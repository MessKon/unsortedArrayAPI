# Unsorted Array App
This repository contains a Python application that provides an API for processing data.
Given an unsorted array as an input, the app will print all unique pairs in the unsorted array with equal sum.
The API is built using Flask and is designed to be simple and easy to deploy using Docker.

In addition to the application itself, the repository also includes:

- A Dockerfile to containerize the app
- Terraform scripts for infrastructure setup (like DynamoDB)
- GitHub Actions workflows for CI/CD
- Makefile targets for simplifying common tasks


## Features
- A REST API that listens for POST requests and processes the data
- Integration with DynamoDB for logging requests (optional)
- Docker support for easy local development and deployment
- CI/CD integration via GitHub Actions


## Makefile Targets
The Makefile in this repository provides few useful targets for common tasks such as building, running, and pushing Docker images. Below are the available targets and their usage:


#### Running the App on the Dev Machine

This target sets up a virtual environment, installs the required dependencies, and starts the Flask app locally.

```bash
make run-dev
```

This command will:
- Create a Python virtual environment in the venv/ directory
- Install dependencies from requirements.txt
- Run the app on your local machine, accessible via `http://localhost:5000`


#### Building the Docker Image

This target builds the Docker image using the provided Dockerfile

```bash
make build
```

This command will:
- Build the Docker image for the app and tag it as latest


#### Pushing the Docker Image

This target pushes the built Docker image to the Docker registry (e.g., Docker Hub).

```bash
make push
```

This command will:
- Tag the local image with the appropriate tag for the Docker registry
- Push the image to the registry


#### Running the App Inside a Docker Container

This target runs the app in a Docker container, exposing the app on a given port (default `5000`) of the host machine.

```bash
make run-container
```

This command will:
- Run the app within a  Docker container with the latest tag
- Expose the app on a given port (default `5000`) of your local machine


#### Build and Push the Docker Image
This target combines the build and push targets to streamline the process of building and pushing the Docker image.

```bash
make build-and-push
```

This command will:
- Build the Docker image
- Push the image to the Docker registry (e.g., Docker Hub)
