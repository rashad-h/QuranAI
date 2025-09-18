from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
import json
import httpx
from mangum import Mangum
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="QuranAI API", version="1.0.0")

# CORS middleware for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class QuranQuestionRequest(BaseModel):
    ayah_or_reference: str
    question: Optional[str] = ""

class QuranQuestionResponse(BaseModel):
    summary: str
    word_by_word: List[str]
    references: List[str]

class FiqhQuestionRequest(BaseModel):
    question: str
    madhhab: str

class FiqhQuestionResponse(BaseModel):
    answer: str
    steps: List[str]
    references: List[str]

# OpenAI API configuration
openai_api_key = os.getenv("OPENAI_API_KEY")
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

async def call_openai(prompt: str, max_tokens: int = 500) -> str:
    """Call OpenAI API directly with httpx"""
    try:
        if not openai_api_key:
            return "OpenAI API key not configured"
        
        headers = {
            "Authorization": f"Bearer {openai_api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": 0.7
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(OPENAI_API_URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                print(f"OpenAI API error: {response.status_code} - {response.text}")
                return f"OpenAI API error: {response.status_code}"
                
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Error calling AI service"

@app.get("/")
async def root():
    return {"message": "QuranAI API is running"}

@app.post("/quran_question", response_model=QuranQuestionResponse)
async def ask_quran_question(request: QuranQuestionRequest):
    """
    Endpoint for Quran Q&A - provides tafsir, word-by-word translation, and references
    """
    try:
        # Construct the AI prompt
        prompt = f"""You are an Islamic scholar AI. User provides: "{request.ayah_or_reference}" and asks: "{request.question}"

1. Provide a concise tafsir summary in simple English.
2. Provide word-by-word translation if applicable.
3. Cite authentic sources (Ibn Kathir, Tafsir al-Jalalayn).
4. Keep response under 200 words for UI card display.

Return your response in this exact JSON format:
{{
  "summary": "Your tafsir explanation here",
  "word_by_word": ["word1", "translation1", "word2", "translation2"],
  "references": ["Source 1", "Source 2"]
}}"""

        # Call OpenAI API
        ai_response = await call_openai(prompt)
        
        # Try to parse JSON response, fallback to placeholder if parsing fails
        try:
            # Clean the response - sometimes AI adds extra text around JSON
            cleaned_response = ai_response.strip()
            if cleaned_response.startswith('{') and cleaned_response.endswith('}'):
                response_data = json.loads(cleaned_response)
            else:
                # Try to extract JSON from the response
                start_idx = cleaned_response.find('{')
                end_idx = cleaned_response.rfind('}') + 1
                if start_idx != -1 and end_idx != 0:
                    json_str = cleaned_response[start_idx:end_idx]
                    response_data = json.loads(json_str)
                else:
                    raise json.JSONDecodeError("No JSON found", ai_response, 0)
            
            return QuranQuestionResponse(
                summary=response_data.get("summary", "Unable to process response"),
                word_by_word=response_data.get("word_by_word", []),
                references=response_data.get("references", [])
            )
        except json.JSONDecodeError:
            # Fallback response if AI doesn't return proper JSON
            return QuranQuestionResponse(
                summary=ai_response if ai_response else f"Analysis of {request.ayah_or_reference}: This ayah contains important Islamic guidance and principles for believers.",
                word_by_word=["Allah", "God", "Rahman", "Most Merciful", "Rahim", "Most Compassionate"],
                references=["Tafsir Ibn Kathir", "Tafsir al-Jalalayn"]
            )
        
    except Exception as e:
        return QuranQuestionResponse(
            summary="Error processing your question. Please try again.",
            word_by_word=[],
            references=[]
        )

@app.post("/fiqh_question", response_model=FiqhQuestionResponse)
async def ask_fiqh_question(request: FiqhQuestionRequest):
    """
    Endpoint for Fiqh Assistant - provides rulings according to selected madhhab
    """
    try:
        # Construct the AI prompt
        prompt = f"""You are an Islamic fiqh expert AI. User asks: "{request.question}" according to {request.madhhab} madhhab.

1. Give a concise ruling according to the {request.madhhab} madhhab.
2. Include step-by-step guidance if relevant.
3. Provide references from trusted fiqh books.
4. Keep answers clear and structured for display in a card UI.

Return your response in this exact JSON format:
{{
  "answer": "The ruling according to {request.madhhab} madhhab is...",
  "steps": ["Step 1", "Step 2", "Step 3"],
  "references": ["Fiqh Book Reference 1", "Fiqh Book Reference 2"]
}}"""

        # Call OpenAI API
        ai_response = await call_openai(prompt)
        
        # Try to parse JSON response, fallback to placeholder if parsing fails
        try:
            # Clean the response - sometimes AI adds extra text around JSON
            cleaned_response = ai_response.strip()
            if cleaned_response.startswith('{') and cleaned_response.endswith('}'):
                response_data = json.loads(cleaned_response)
            else:
                # Try to extract JSON from the response
                start_idx = cleaned_response.find('{')
                end_idx = cleaned_response.rfind('}') + 1
                if start_idx != -1 and end_idx != 0:
                    json_str = cleaned_response[start_idx:end_idx]
                    response_data = json.loads(json_str)
                else:
                    raise json.JSONDecodeError("No JSON found", ai_response, 0)
            
            return FiqhQuestionResponse(
                answer=response_data.get("answer", "Unable to process response"),
                steps=response_data.get("steps", []),
                references=response_data.get("references", [])
            )
        except json.JSONDecodeError:
            # Fallback response if AI doesn't return proper JSON
            return FiqhQuestionResponse(
                answer=ai_response if ai_response else f"According to the {request.madhhab} madhhab: This matter requires careful consideration of Islamic principles and the specific circumstances involved.",
                steps=[
                    "Assess the specific situation and context",
                    "Consider the relevant Islamic principles",
                    "Apply the madhhab's methodology",
                    "Seek additional guidance if needed"
                ],
                references=[f"{request.madhhab} Fiqh Manual", "Classical Fiqh Text"]
            )
        
    except Exception as e:
        return FiqhQuestionResponse(
            answer="Error processing your question. Please try again.",
            steps=[],
            references=[]
        )

# AWS Lambda handler using Mangum
handler = Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
