# Better use newer Python as generated code can use new features
FROM python:3.10-slim

# install git
RUN apt-get update && apt-get install -y git && apt-get clean

# upgrade to latest pip
RUN pip install --upgrade pip

COPY . .

RUN cd /human-eval && pip install .

WORKDIR /human-eval

ENTRYPOINT ["python3", "-m", "human_eval.evaluation"]