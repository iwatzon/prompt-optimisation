
prefix = "Solve the following maths word problem: "
suffix = "Please output your answer at the end as ##<your answer (arabic numerals)>"

def get_baseline_prompt():
   return prefix+"\n{content}\n"+suffix
   
def get_criteria():
   return """- The prompt MUST instruct the LLM to solve a maths word problem.
- The prompt MUST include the content placeholder (this is where the maths word problem will be).
- The prompt MUST instruct the model to output the answer at the end as ##<your answer (arabic numerals)> with no spaces."""
   
def get_emotive_prompt():
   return prefix+"\n{content}\nThis is very important to my career.\n"+suffix

def get_CoT_prompt():
   return prefix+"\n{content}\nLet's think step by step.\n"+suffix