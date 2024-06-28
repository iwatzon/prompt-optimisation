# https://github.com/openai/human-eval/blob/master/human_eval/execution.py

from typing import Optional, Dict
import multiprocessing
import tempfile
import subprocess
import tempfile

def check_correctness(problem: Dict, completion: str, timeout: float, completion_id: Optional[int] = None) -> Dict:
    # Usage within check_correctness
    manager = multiprocessing.Manager()
    result = manager.list()

    executor = DockerExecutor(problem, completion, timeout + 1, result)
    p = multiprocessing.Process(target=executor)
    p.start()
    p.join(timeout=timeout + 1)
    if p.is_alive():
        p.kill()

    if not result:
        result.append("timed out")

    return dict(
        task_id=problem["task_id"],
        passed=result[0] == "passed",
        result=result[0],
        completion_id=completion_id,
    )

class DockerExecutor:
    def __init__(self, problem, completion, timeout, result):
        self.problem = problem
        self.completion = completion
        self.timeout = timeout
        self.result = result

    def __call__(self):
        # Call the execute_in_docker function
        stdout, stderr = self.execute_in_docker(self.problem, self.completion, self.timeout)

        # Interpret the results
        if stdout is None and stderr == "Timed out":
            self.result.append("timed out")
        elif stderr:
            self.result.append(f"failed: {stderr}")
        else:
            self.result.append("passed")

    def execute_in_docker(self, problem, completion, timeout):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py') as tmpfile:
            # Write the code to a temp file
            code = problem["prompt"] + completion + "\n" + problem["test"] + "\n" + f"check({problem['entry_point']})"
            tmpfile.write(code)
            tmpfile.flush()

            # Construct Docker command
            docker_cmd = [
                "docker", "run"#, "--rm",
                "--network", "none",
                "--memory", "128m",
                "--cpus", ".5",
                "--volume", f"{tmpfile.name}:/sandbox/code.py:ro",
                "my_python_sandbox",
                "python", "/sandbox/code.py"
            ]

            try:
                # Execute the Docker command
                result = subprocess.run(docker_cmd, timeout=timeout + 1, capture_output=True, text=True)
                return result.stdout, result.stderr
            except subprocess.TimeoutExpired:
                return None, "Timed out"