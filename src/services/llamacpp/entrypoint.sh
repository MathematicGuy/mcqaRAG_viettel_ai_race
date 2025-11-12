#!/bin/bash
set -e

MODEL=${OLLAMA_MODEL:-qwen3:1.7b}

# 1. Khởi động Ollama server trong background
echo "Starting Ollama server..."
ollama serve &

# 2. Đợi server sẵn sàng
echo "Waiting for Ollama server to be ready..."
until ollama list > /dev/null 2>&1; do
    echo "Waiting..."
    sleep 2
done
echo "Ollama server is ready!"

# 3. Pull model (bây giờ server đã chạy)
echo "Pulling model $MODEL..."
if ! ollama list | grep -q "$MODEL"; then
    ollama pull "$MODEL"
    echo "Model $MODEL pulled successfully!"
else
    echo "Model $MODEL already exists."
fi

# 4. Giữ container chạy
wait