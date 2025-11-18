Local AI Document Summarizer

A simple, private tool to summarize text and PDF documents locally using Ollama and Llama 3.

This project runs a Large Language Model (LLM) inside a Docker container, ensuring your data stays on your machine.

Features

100% Private: No data is sent to the cloud.

Easy Setup: Runs cleanly in Docker.

GPU Supported: Fast inference with NVIDIA GPUs.

Multi-Format: Supports .txt and .pdf files.

Prerequisites

Docker & Docker Compose

Python 3.8+

NVIDIA Container Toolkit (Linux/GPU users)

Installation

Clone the repo:

git clone [https://github.com/yourusername/local-summarizer.git](https://github.com/yourusername/local-summarizer.git)
cd local-summarizer


Start Ollama:

make up


Download Model (Llama 3):

make pull


Install Python Requirements:

pip install ollama pypdf


Usage

Ensure the server is running (make up), then summarize a file:

python summarizer.py notes.txt


or

python summarizer.py document.pdf


Helper Commands

Command

Description

make up

Start server.

make down

Stop server.

make logs

View logs.

make pull

Download default model.

make chat

Chat interactively.

make prune

Delete everything (data included).

Configuration

Change Model: Run make pull model=mistral (remember to update summarizer.py).

CPU Mode: Remove the deploy: section in docker-compose.yml if you don't have an NVIDIA GPU.
