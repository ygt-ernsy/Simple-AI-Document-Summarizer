# 🤖 Local AI Document Summarizer

A simple, private tool to summarize text and PDF documents locally using Ollama and Llama 3.

This project runs a Large Language Model (LLM) inside a Docker container, ensuring your data stays on your machine.

---

## ✨ Features

- **🔒 100% Private**: No data is sent to the cloud
- **⚡ Easy Setup**: Runs cleanly in Docker
- **🚀 GPU Supported**: Fast inference with NVIDIA GPUs
- **📄 Multi-Format**: Supports `.txt` and `.pdf` files

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.8+
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) (Linux/GPU users only)

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/local-summarizer.git
cd local-summarizer
```

### 2. Start Ollama server

```bash
make up
```

### 3. Download the model (Llama 3)

```bash
make pull
```

### 4. Install Python dependencies

```bash
pip install ollama pypdf
```

---

## 🚀 Usage

Ensure the server is running (`make up`), then summarize a file:

### Summarize a text file

```bash
python summarizer.py notes.txt
```

### Summarize a PDF document

```bash
python summarizer.py document.pdf
```

---

## 📖 Helper Commands

| Command | Description |
|---------|-------------|
| `make up` | Start the Ollama server |
| `make down` | Stop the Ollama server |
| `make logs` | View server logs |
| `make pull` | Download the default model (Llama 3) |
| `make chat` | Start an interactive chat session |
| `make prune` | Delete everything (including data) |

---

## ⚙️ Configuration

### Change the Model

To use a different model (e.g., Mistral):

```bash
make pull model=mistral
```

**Note**: Remember to update `summarizer.py` to reference the new model.

### CPU-Only Mode

If you don't have an NVIDIA GPU, remove the `deploy:` section from `docker-compose.yml` to run in CPU mode.
