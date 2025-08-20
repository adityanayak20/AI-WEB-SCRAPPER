#!/bin/bash
set -e

echo "🔄 Rebuilding Docker images..."
docker compose build --no-cache

echo "🚀 Starting services..."
docker compose up -d

echo "⏳ Waiting for Ollama to start..."
sleep 10

echo "📦 Pulling llama3:latest model (if not already present)..."
docker exec -it ollama ollama pull llama3:latest || true

echo "✅ App running at: http://localhost:8501"
echo "📜 Showing scraper logs (Ctrl+C to stop viewing)..."
docker compose logs -f scraper