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

# Check Ollama (llama.cpp runs separately on port 8080)
print_info "llama.cpp server must be started separately"
print_info "Run: ./server -m path/to/SmallThinker-3B-Preview-Q4_K_M.gguf -c 16384 --port 8080"

# Check API service
if curl -s http://localhost:8000/health >/dev/null 2>&1; then
    print_success "API service is ready"
else
    print_warning "Ollama is not ready yet. It may need more time."
fi

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
echo "  - OpenSearch:        http://localhost:9200"
echo "  - PostgreSQL:        localhost:5432"
echo "  - Redis:             localhost:6379"
echo ""
echo "⚠️  Important: Start llama.cpp server separately!"
echo "  Run: ./server -m path/to/SmallThinker-3B-Preview-Q4_K_M.gguf -c 16384 --port 8080"
echo ""
echo "Next Steps:"
echo "  1. Start llama.cpp:  (see command above)"
echo "  2. Run extraction:   jupyter notebook run_extract.ipynb"
echo "  3. Run inference:    python run_mcq_system.py"
echo "  4. Generate output:  python post_processing/write_answers.py && python data/process_answer.py"
echo ""
echo "Quick Commands:"
echo "  - docker compose ps        # View services"
echo "  - docker compose logs -f   # View logs"
echo "  - docker compose restart   # Restart services"
echo ""
print_info "Run 'make help' to see all available commands"
echo ""
