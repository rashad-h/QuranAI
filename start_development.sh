#!/bin/bash

echo "🚀 Starting QuranAI Development Environment"

# Start backend
echo "📡 Starting FastAPI backend..."
cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install requirements
source venv/bin/activate
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    cp env.example .env
    echo "Created .env file from env.example"
fi

python3 main.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 3

# Start frontend
echo "🎨 Starting Vue frontend..."
cd ../frontend
npm install
npm run dev &
FRONTEND_PID=$!

echo "✅ Development servers started!"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for interrupt
trap "kill $BACKEND_PID $FRONTEND_PID" INT
wait
