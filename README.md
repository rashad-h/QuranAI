# QuranAI - Islamic Study Assistant

A minimal Vue + FastAPI application for Quran Q&A and Fiqh assistance.

## 🚀 Quick Start

### Backend (FastAPI)

1. Navigate to backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp env.example .env
# Edit .env and add your OpenAI API key
```

4. Run locally:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend (Vue 3)

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run development server:
```bash
npm run dev
```

4. Build for production:
```bash
npm run build
```

## 🌐 Deployment

### Backend - AWS Lambda

1. Install AWS CLI and configure credentials
2. Package your FastAPI app:
```bash
zip -r lambda-deployment.zip main.py requirements.txt
```
3. Deploy to AWS Lambda with API Gateway
4. Update the `API_BASE_URL` in frontend components

### Frontend - GitHub Pages

1. Build the project:
```bash
npm run build
```

2. Deploy the `dist/` folder to GitHub Pages

## 📁 Project Structure

```
QuranAI/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── env.example         # Environment variables template
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── QuranQA.vue     # Quran Q&A component
│   │   │   └── FiqhAssistant.vue # Fiqh assistant component
│   │   ├── App.vue             # Main Vue app
│   │   ├── main.js             # Vue app entry point
│   │   └── style.css           # Tailwind CSS imports
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
└── README.md
```

## 🔧 Features

### Quran Q&A
- Ask questions about specific ayahs or general Quran topics
- Get tafsir summaries with word-by-word translations
- View authentic scholarly references

### Fiqh Assistant
- Select your preferred madhhab (Hanafi, Shafi'i, Maliki, Hanbali)
- Ask practical Islamic jurisprudence questions
- Get step-by-step guidance with scholarly references

## 🎨 Tech Stack

- **Frontend**: Vue 3, Tailwind CSS, Vite
- **Backend**: FastAPI, Python
- **AI**: OpenAI API (or local LLM)
- **Deployment**: AWS Lambda + API Gateway, GitHub Pages

## 📝 API Endpoints

### POST /quran_question
Request:
```json
{
  "ayah_or_reference": "Surah 2:255",
  "question": "What is the meaning of this ayah?"
}
```

Response:
```json
{
  "summary": "Tafsir explanation...",
  "word_by_word": ["Allah", "God", "Rahman", "Most Merciful"],
  "references": ["Tafsir Ibn Kathir", "Tafsir al-Jalalayn"]
}
```

### POST /fiqh_question
Request:
```json
{
  "question": "What are the conditions for prayer?",
  "madhhab": "Hanafi"
}
```

Response:
```json
{
  "answer": "According to Hanafi madhhab...",
  "steps": ["Step 1", "Step 2", "Step 3"],
  "references": ["Hanafi Fiqh Manual"]
}
```

## 🔑 Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key for AI responses

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
