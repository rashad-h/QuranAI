# QuranAI Setup Guide

## 🚀 Quick Start

### 1. Backend Setup

```bash
cd backend
python3 -m pip install -r requirements.txt
```

Create environment file:
```bash
cp env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_openai_api_key_here
```

### 2. Frontend Setup

```bash
cd frontend
npm install
```

### 3. Run Development Servers

**Option A: Use the startup script (runs both backend and frontend)**
```bash
./start_development.sh
```

**Option B: Run separately**

Backend:
```bash
cd backend
python3 main.py
```

Frontend (in new terminal):
```bash
cd frontend
npm run dev
```

## 🌐 Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📡 Deployment

### Backend - AWS Lambda

1. **Package for deployment:**
```bash
cd backend
python3 lambda_deploy.py
```

2. **Deploy to AWS:**
   - Upload `lambda-deployment.zip` to AWS Lambda
   - Set handler to: `main.handler`
   - Add environment variable: `OPENAI_API_KEY`
   - Create API Gateway trigger

3. **Update frontend config:**
   - Edit `frontend/src/config.js`
   - Replace `BASE_URL` with your Lambda API Gateway URL

### Frontend - GitHub Pages

1. **Build the project:**
```bash
cd frontend
npm run build
```

2. **Deploy:**
   - Push your code to GitHub
   - Enable GitHub Pages in repository settings
   - The GitHub Action will automatically deploy from `main` branch

## 🔧 Configuration

### API Endpoints
Edit `frontend/src/config.js` to change API endpoints:

```javascript
export const API_CONFIG = {
  // For local development
  BASE_URL: 'http://localhost:8000',
  
  // For production (replace with your Lambda URL)
  // BASE_URL: 'https://your-api-gateway-url.amazonaws.com/prod',
}
```

### Environment Variables

**Backend (.env):**
- `OPENAI_API_KEY`: Your OpenAI API key

## 🎯 Features

### Quran Q&A Tab
- Enter surah/ayah reference (optional)
- Ask questions about Quranic verses
- Get tafsir summaries with word-by-word translations
- View scholarly references

### Fiqh Assistant Tab
- Select your preferred madhhab
- Ask practical Islamic jurisprudence questions
- Get step-by-step guidance
- View scholarly references

## 🛠️ Tech Stack

- **Frontend**: Vue 3, Tailwind CSS, Vite
- **Backend**: FastAPI, Python
- **AI**: OpenAI GPT-3.5-turbo
- **Deployment**: AWS Lambda, GitHub Pages

## 📝 API Documentation

When running locally, visit http://localhost:8000/docs for interactive API documentation.

## 🤝 Need Help?

- Check the main README.md for more details
- Review the code comments for implementation details
- Test the API endpoints using the interactive docs at `/docs`
