APP_NAME := unsorted-array-app
IMAGE_NAME := docker.io/messkon/$(APP_NAME):latest
DOCKERFILE := Dockerfile
SRC_DIR := src
PORT := 5000

.PHONY: run-dev build push run-container build-and-push

run-dev:
	@echo "Running the app on the development machine..."
	python3 -m venv venv && . venv/bin/activate && pip install -r $(SRC_DIR)/requirements.txt
	PYTHONPATH=$(SRC_DIR) python $(SRC_DIR)/app.py

build:
	@echo "Building Docker image..."
	docker build -t $(APP_NAME):latest -f $(DOCKERFILE) .

push: build
	@echo "Pushing Docker image to the registry..."
	docker tag $(APP_NAME):latest $(IMAGE_NAME)
	docker push $(IMAGE_NAME)

build-and-push: build push
	@echo "Build and push completed."

run-container:
	@echo "Running the app in a Docker container..."
	docker run --rm -p $(PORT):5000 $(APP_NAME):latest
