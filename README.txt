# Garden Advice Docker Submission

This project containerises the Garden Advice console-based Python program.

## Files
- garden_advice.py - Python console application
- Dockerfile - instructions for building the Docker image
- docker1.txt - Docker Hub repository link

## Build the Docker image

Run these commands from this folder:

docker build -t garden-app .

## Test the container

Because the program asks for keyboard input, use:

docker run -i garden-app

## Log in to Docker Hub

docker login

## Tag the image

Replace YOUR-DOCKERHUB-USERNAME with your actual Docker Hub username:

docker tag garden-app YOUR-DOCKERHUB-USERNAME/garden-app

## Push the image

docker push YOUR-DOCKERHUB-USERNAME/garden-app

## Docker Playground test

On Docker Playground, pull the image:

docker pull YOUR-DOCKERHUB-USERNAME/garden-app

Then run it:

docker run -i YOUR-DOCKERHUB-USERNAME/garden-app

The program should ask for the season and plant type and then display gardening advice.
