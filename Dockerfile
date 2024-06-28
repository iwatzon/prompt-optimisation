# Use an official Python 3.11 image as a base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /sandbox

# Install poetry
RUN pip install poetry

# Copy only the files necessary for installing dependencies to avoid rebuilding the image unnecessarily
COPY pyproject.toml poetry.lock* /sandbox/

# Install project dependencies (without dev dependencies to keep the image small)
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Ensure UTF-8 encoding in Python
ENV PYTHONIOENCODING=UTF-8

# The container does nothing by default, waiting for commands
CMD ["bash"]
