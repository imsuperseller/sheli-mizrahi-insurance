#!/bin/bash

echo "🏠 Starting Sheli Mizrahi Insurance System..."
echo "📍 Location: Afula, Israel"
echo "🎨 Theme: Blue (differentiated from Tax4US green, Rensto branding)"

# Set environment variables
export INSURANCE_USERNAME="shelimizrahi"
export INSURANCE_PASSWORD="insurance2024"
export OPENAI_API_KEY="your_openai_api_key_here"

echo "📦 Installing Python dependencies..."
cd insurance-api
pip install -r requirements.txt

echo "🌐 Starting FastAPI server on http://localhost:8001"
echo "📚 API Documentation: http://localhost:8001/docs"
echo "🔗 MCP Endpoint: http://localhost:8001/mcp"

# Start the FastAPI server
uvicorn app:app --host 0.0.0.0 --port 8001 --reload
