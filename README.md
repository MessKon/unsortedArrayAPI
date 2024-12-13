# Unsorted Array App
This repository contains a Python application that provides an API for processing data.
Given an unsorted array as an input, the app will print all unique pairs in the unsorted array with equal sum.
The API is built using Flask and is designed to be simple and easy to deploy using Docker.

In addition to the application itself, the repository also includes:

- A Dockerfile to containerize the app
- Terraform scripts for infrastructure setup (like DynamoDB)
- GitHub Actions workflows for CI/CD
- Makefile targets for simplifying common tasks
- Kubernetes manifests for local Minikube deployment


## Features
- A REST API that listens for POST requests and processes the data
- Integration with DynamoDB for logging requests (optional)
- Docker support for easy local development and deployment
- Kubernetes support for deployment on local clusters - **Assumes minikbe has been installed locally**
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


#### Deploy the App to Minikube
This target deploys your app to a local Minikube Kubernetes cluster. It will apply all the necessary Kubernetes manifests (namespace, configmap, deployment, service) to the cluster.

```bash
make deploy-kubernetes
```

This command will:
- Build the Docker image
- Ensure Minikube is started
- Apply the namespace, configMap, deployment, and service manifests to deploy the app to the Minikube cluster

Once this target has been executed, one can use `kubectl port-forward` to expose the app to a local port as:
```bash
kubectl -n dev port-forward service/unsorted-array-app-svc 5000:5000
```

If on the minikube cluster the app image cannot be downloaded you might have to use:
```bash
eval $(minikube -p minikube docker-env)
```

To clean-up the cluster, simply run:
```bash
minikube delete
```


## Suggestions for Improvements
The repo currently holds a simplistic approach to the implementation.
A couple of things that could be improved are:
- Use of `tflocal` for local testing with DynamoDB. More specifically, attempts of using `tflocal` to deploy the DynamoDB and get the app to use it, did not succeed. In order to keep this implementation within a reasonable time-frame, the in-memory-store alternative was implemented
- Adding a Helm chart to make the app deployable on Kubernetes, using Helm
