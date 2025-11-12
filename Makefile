# Makefile for RAG MCQ System
# Provides convenient commands for common operations

.PHONY: help install start stop restart status logs clean test format lint health pull-model

# Default target
.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "RAG MCQ System - Available Commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Setup and Installation
install: ## Install Python dependencies with UV
	@echo "Installing dependencies with UV..."
	uv sync
	@echo "✓ Dependencies installed"

install-dev: ## Install with dev dependencies
	@echo "Installing with dev dependencies..."
	uv sync --extra dev --extra notebook
	@echo "✓ Dev dependencies installed"

# Docker Operations
start: ## Start all Docker services
	@echo "Starting all services..."
	docker compose up -d
	@echo "✓ Services started"
	@echo "Waiting for services to be healthy..."
	@sleep 10
	@make status

stop: ## Stop all Docker services
	@echo "Stopping all services..."
	docker compose down
	@echo "✓ Services stopped"

restart: ## Restart all Docker services
	@echo "Restarting all services..."
	docker compose restart
	@echo "✓ Services restarted"

build: ## Build Docker images
	@echo "Building Docker images..."
	docker compose build
	@echo "✓ Images built"

clean: ## Clean up Docker resources (volumes, networks)
	@echo "Cleaning up Docker resources..."
	docker compose down -v
	@echo "✓ Cleanup complete"

status: ## Show status of all services
	@echo "Service Status:"
	@docker compose ps

logs: ## Show logs from all services
	docker compose logs -f

logs-api: ## Show logs from API service
	docker compose logs -f api

# logs-airflow: ## Show logs from Airflow
# 	docker compose logs -f airflow

logs-opensearch: ## Show logs from OpenSearch
	docker compose logs -f opensearch

# Health Checks
health: ## Check health of all services
	@echo "Checking service health..."
	@echo ""
	@echo "API Health:"
	@curl -s http://localhost:8000/health | python -m json.tool || echo "API not ready"
	@echo ""
	@echo "PostgreSQL:"
	@docker exec rag-mcq-postgres pg_isready -U rag_user || echo "PostgreSQL not ready"
	@echo ""
	@echo "OpenSearch:"
	@curl -s http://localhost:9200/_cluster/health | python -m json.tool || echo "OpenSearch not ready"
	@echo ""
	@echo "Redis:"
	@docker exec rag-mcq-redis redis-cli ping || echo "Redis not ready"
	@echo ""
	@echo "⚠️  llama.cpp (port 8080): Must be started manually"
	@echo ""

# Ollama Model Management - DISABLED (using llama.cpp instead)
# Start llama.cpp manually:
# ./server -m "path/to/SmallThinker-3B-Preview-Q4_K_M.gguf" -c 16384 --port 8080 --host 127.0.0.1

# Database Operations
db-init: ## Initialize database schema
	@echo "Initializing database..."
	uv run alembic upgrade head
	@echo "✓ Database initialized"

db-reset: ## Reset database (WARNING: deletes all data)
	@echo "Resetting database..."
	docker compose down postgres
	docker volume rm rag_mcq_system_postgres_data || true
	docker compose up -d postgres
	@sleep 5
	@make db-init
	@echo "✓ Database reset complete"

db-shell: ## Open PostgreSQL shell
	docker exec -it rag-mcq-postgres psql -U rag_user -d rag_mcq_db

# OpenSearch Operations
opensearch-status: ## Check OpenSearch cluster status
	@curl -s http://localhost:9200/_cluster/health | python -m json.tool

opensearch-indices: ## List OpenSearch indices
	@curl -s http://localhost:9200/_cat/indices?v

opensearch-delete-index: ## Delete OpenSearch index (INDEX=mcq-documents)
	@echo "Deleting index: $(INDEX)"
	@curl -X DELETE http://localhost:9200/$(INDEX)
	@echo ""
	@echo "✓ Index deleted"

# Redis Operations
redis-shell: ## Open Redis CLI
	docker exec -it rag-mcq-redis redis-cli

redis-flush: ## Flush Redis cache
	docker exec rag-mcq-redis redis-cli FLUSHALL
	@echo "✓ Redis cache cleared"

redis-info: ## Show Redis info
	docker exec rag-mcq-redis redis-cli INFO

# Testing
test: ## Run all tests
	@echo "Running tests..."
	uv run pytest
	@echo "✓ Tests complete"

test-cov: ## Run tests with coverage
	@echo "Running tests with coverage..."
	uv run pytest --cov=src --cov-report=html --cov-report=term
	@echo "✓ Coverage report generated in htmlcov/"

test-watch: ## Run tests in watch mode
	uv run pytest-watch

# Code Quality
format: ## Format code with ruff
	@echo "Formatting code..."
	uv run ruff format src/ tests/
	@echo "✓ Code formatted"

lint: ## Lint code with ruff
	@echo "Linting code..."
	uv run ruff check src/ tests/
	@echo "✓ Linting complete"

lint-fix: ## Fix linting issues automatically
	@echo "Fixing linting issues..."
	uv run ruff check --fix src/ tests/
	@echo "✓ Issues fixed"

type-check: ## Run type checking with mypy
	@echo "Running type checks..."
	uv run mypy src/
	@echo "✓ Type checking complete"

# Development
dev: ## Start development environment
	@make start
	@make db-init
	@echo ""
	@echo "✓ Development environment ready!"
	@echo ""
	@echo "Services:"
	@echo "  API:        http://localhost:8000"
	@echo "  API Docs:   http://localhost:8000/docs"
	@echo "  OpenSearch: http://localhost:9200"
	@echo ""
	@echo "⚠️  Important: Start llama.cpp separately!"
	@echo "  Run: ./server -m path/to/SmallThinker-3B-Preview-Q4_K_M.gguf -c 16384 --port 8080"
	@echo ""

notebook: ## Start Jupyter notebook server
	@echo "Starting Jupyter notebook..."
	uv run jupyter notebook

# Airflow Operations - DISABLED (not used in current implementation)

# Monitoring
monitor: ## Start monitoring services (Langfuse)
	@echo "Starting monitoring services..."
	docker compose --profile monitoring up -d
	@echo "✓ Langfuse available at http://localhost:3000"

# Quick Commands
quick-test: ## Quick test of the system
	@echo "Running quick system test..."
	@echo ""
	@echo "1. Testing API health..."
	@curl -s http://localhost:8000/health | python -m json.tool | grep status || echo "API not ready"
	@echo ""
	@echo "2. Testing search endpoint..."
	@curl -s -X POST http://localhost:8000/api/v1/search \
		-H "Content-Type: application/json" \
		-d '{"query": "test", "top_k": 1}' | python -m json.tool || echo "Search not ready"
	@echo ""
	@echo "✓ Quick test complete"

# Documentation
docs: ## Generate documentation
	@echo "Generating documentation..."
	@echo "API docs available at http://localhost:8000/docs"

# Full Setup
setup-full: ## Complete setup from scratch
	@echo "Starting full setup..."
	@make install-dev
	@make start
	@sleep 15
	@make db-init
	@make health
	@echo ""
	@echo "✓ Full setup complete!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Start llama.cpp:  ./server -m path/to/model.gguf -c 16384 --port 8080"
	@echo "  2. Run extraction:   jupyter notebook run_extract.ipynb"
	@echo "  3. Run inference:    python run_mcq_system.py"
	@echo "  4. View API docs:    http://localhost:8000/docs"
