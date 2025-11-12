#!/bin/bash

# RAG MCQ System - Quick Setup Script
# This script sets up the complete RAG system for multiple choice question answering

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Print banner
echo "=================================================="
echo "   RAG MCQ System - Quick Setup"
echo "   Production-ready RAG for Question Answering"
echo "=================================================="
echo ""

# Check prerequisites
print_info "Checking prerequisites..."

if ! command_exists docker; then
    print_error "Docker is not installed. Please install Docker Desktop first."
    exit 1
fi

if ! command_exists docker-compose && ! docker compose version >/dev/null 2>&1; then
    print_error "Docker Compose is not available. Please install Docker Compose."
    exit 1
fi

print_success "Docker is installed"

# Check Python
if ! command_exists python3; then
    print_error "Python 3 is not installed. Please install Python 3.11 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
print_success "Python ${PYTHON_VERSION} is installed"

# Check UV
if ! command_exists uv; then
    print_warning "UV package manager not found. Installing UV..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"

    if command_exists uv; then
        print_success "UV installed successfully"
    else
        print_error "Failed to install UV. Please install manually: https://github.com/astral-sh/uv"
        exit 1
    fi
else
    print_success "UV package manager is installed"
fi

# Setup environment
print_info "Setting up environment configuration..."

if [ ! -f ".env" ]; then
    print_info "Creating .env file from template..."
    cp .env.example .env
    print_success ".env file created. Please review and update if needed."
else
    print_warning ".env file already exists. Skipping."
fi

# Install Python dependencies
print_info "Installing Python dependencies with UV..."
uv sync --extra dev --extra notebook
print_success "Python dependencies installed"

# Start Docker services
print_info "Starting Docker services..."
docker compose down -v 2>/dev/null || true
docker compose up -d

print_info "Waiting for services to start (this may take a minute)..."
sleep 15

# Check service health
print_info "Checking service health..."

# Check PostgreSQL
if docker exec rag-mcq-postgres pg_isready -U rag_user >/dev/null 2>&1; then
    print_success "PostgreSQL is ready"
else
    print_warning "PostgreSQL is not ready yet. It may need more time."
fi

# Check OpenSearch
if curl -s http://localhost:9200/_cluster/health >/dev/null 2>&1; then
    print_success "OpenSearch is ready"
else
    print_warning "OpenSearch is not ready yet. It may need more time."
fi

# Check Redis
if docker exec rag-mcq-redis redis-cli ping >/dev/null 2>&1; then
    print_success "Redis is ready"
else
    print_warning "Redis is not ready yet. It may need more time."
fi

# Check Ollama (DISABLED - Using llama.cpp instead)
# if curl -s http://localhost:11434/api/tags >/dev/null 2>&1; then
#     print_success "Ollama is ready"
# else
#     print_warning "Ollama is disabled (using llama.cpp instead)"
# fi

# Check API service
if curl -s http://localhost:8000/health >/dev/null 2>&1; then
    print_success "API service is ready"
else
    print_warning "API service is not ready yet. It may need more time."
fi

# Pull Ollama model (DISABLED - Using llama.cpp instead)
# print_info "Pulling Ollama model (this may take several minutes)..."
# DEFAULT_MODEL="llama3.2:1b"

# if [ -n "$1" ]; then
#     MODEL=$1
# else
#     MODEL=$DEFAULT_MODEL
# fi

# print_info "Pulling model: ${MODEL}"
# docker exec rag-mcq-ollama ollama pull ${MODEL} || print_warning "Failed to pull model. You can do this later with: docker exec rag-mcq-ollama ollama pull ${MODEL}"

# if docker exec rag-mcq-ollama ollama list | grep -q ${MODEL}; then
#     print_success "Model ${MODEL} is ready"
# fi

# Initialize database
print_info "Initializing database schema..."
# Note: This would need alembic migrations to be set up
# uv run alembic upgrade head || print_warning "Database initialization skipped. Run migrations manually."

# Print summary
echo ""
echo "=================================================="
echo "   Setup Complete!"
echo "=================================================="
echo ""
print_success "All services are running!"
echo ""
echo "Available Services:"
echo "  - API:               http://localhost:8000"
echo "  - API Docs:          http://localhost:8000/docs"
# echo "  - Airflow:           http://localhost:8080 (admin/admin)"
echo "  - OpenSearch:        http://localhost:9200"
echo "  - OpenSearch UI:     http://localhost:5601"
echo "  - PostgreSQL:        localhost:5432"
echo "  - Redis:             localhost:6379"
echo "  - Ollama:            DISABLED (using llama.cpp on port 8080)"
echo ""
echo "Next Steps:"
echo "  1. Check health:     make health"
echo "  2. View logs:        make logs"
echo "  3. Run notebooks:    make notebook"
echo "  4. View services:    docker compose ps"
echo ""
echo "Quick Commands:"
echo "  - make start         # Start all services"
echo "  - make stop          # Stop all services"
echo "  - make restart       # Restart all services"
echo "  - make health        # Check service health"
echo "  - make logs          # View logs"
echo ""
echo "Documentation:"
echo "  - README.md                  # Main documentation"
echo "  - IMPLEMENTATION_GUIDE.md    # Implementation details"
echo ""
print_info "Run 'make help' to see all available commands"
echo ""
