# prompt-optimisation

This repo hosts code for prompt-optimisation. This project is an MSc research project exploring autonomous prompt optimisation..

# Basic setup

Please navigate to this [confluence page](https://zilo.atlassian.net/wiki/spaces/AML/pages/138281014/Development+Environment+Setup) for guidance on how to get setup with the development environment:

# Installing the package

To develop # prompt-optimisation:


1. You need python 3.11.x installed on your system.
2. Create a virtual environment using pyenv.
3. Install the pre-commit hooks via `pre-commit install`.
4. Install the package using `poetry install`

To update the dependencies, make any desired changes in `pyproject.toml` and run `poetry update`.

# Creating an env file

In the root folder of the repo, please create an `.env` file containing the correct values for the env vars in the `.env_template`file in the root of the repo.
