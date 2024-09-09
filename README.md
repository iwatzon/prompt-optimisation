# MSs Research Project: Multi-Agent Conversational Architectures for Automated Prompt Engineering

Welcome to the repository for my MSc Research Project titled Multi-Agent Conversational Architectures for Automated Prompt Engineering. This project aims to explore using multi-agent approaches to automate the optimisation of prompts. It uses the concpet of agent roles and core principles to perform domain-specific optimisation and directed prompt refinement. Three multi-agent architectures are evaluated - Authoritarian, Market-Based and Hierarchical - chosen due to the diveristy in agent coordination. 

## Project Structure

The project is organised as follows:

```
├── diagrams/               # Diagrams of multi-agent frameworks
├── human-eval/             # Forked HumanEval repo
├── promptbench/            # Forked rpomptbench repo
├── src/                    # Source code for the project
│   ├── algorithms/         # Notebooks implementing each multi-agent framework
│   ├── conversations/      # Conversations had by the agents during prompt optimisation
│   ├── outputs/            # Raw outputs from evaluation as well as high performing agent interactions
│   ├── prompts/            # Prompts evaluated and success criteria used during optimisation
│   ├── tests/              # Notebooks to perform evaluation and significance testing
│   └── agent_suite.py      # Collection of agents used in the frameworks  
├── Dockerfile              # Dockerfile defining a container for safe execution of code
├── README.md               # This README file
└── requirements.txt        # Python dependencies
```

## Usage

The frameworks can be run within the notebooks in the algorithms file. 
They are setup to perform optimisation for GSM8K, SST-2 and HumanEval, however, can be easily tailored by adding agents to the agent suite and defining a new base prompt and success criteria. The new agents will need to be imported to the notebook script.

Evaluation is completed using the notebooks in the tests folder. HumanEval outputs are evalauted using the run_humaneval notebook, whilst GSM8K and SST-2 are evaluated using the run_promptbench notebook. Significance testing can be done, however, manual input of results is required. 
The run_conversational_analysis notebook using an agent with a JSON viewer tool to read over specified JSONL files containg conversation logs from optimisation processes.

## Results

Raw results using GPT-3.5-Turbo, Mistral-V0.3-7B and Llama-3.1-8B can be seen in the outputs folder, as well as a notebook to visualise them. 
