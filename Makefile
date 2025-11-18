# This sets a default model. You can override it from the command line.
# Example: make pull model=mistral
MODEL ?= llama3:8b

# .PHONY tells Make that these are not files, but command 'targets'
.PHONY: up down logs list pull chat

up:
	@echo "Starting Ollama server..."
	@docker compose up -d

down:
	@echo "Stopping Ollama server..."
	@docker compose down

logs:
	@echo "Following Ollama server logs (Press Ctrl+C to stop)..."
	@docker compose logs -f

list:
	@echo "Listing models downloaded in the 'ollama' container..."
	@docker exec -it ollama ollama list

pull:
	@echo "Pulling model '$(MODEL)' into the 'ollama' container..."
	@docker exec -it ollama ollama pull $(MODEL)

chat:
	@echo "Chatting with model '$(MODEL)' (Type /bye to exit)..."
	@docker exec -it ollama ollama run $(MODEL)
