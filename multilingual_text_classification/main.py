from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from transformers import pipeline
from langdetect import detect, LangDetectException
import logging

# Pydantic model for the input
class TextInput(BaseModel):
    text: str

# Initializing FastAPI app
app = FastAPI()

# logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# transformers pipeline
model_name = "joeddav/xlm-roberta-large-xnli"
classifier = pipeline("zero-shot-classification", model=model_name)

# Defining categories
categories = ["news", "sports", "entertainment", "technology"]

@app.post("/classify/")
async def classify_text(input: TextInput):
    text = input.text
    try:
        # Detect the language
        language = detect(text)
        if language not in ['en', 'es', 'fr']:
            raise HTTPException(status_code=400, detail="Unsupported language")
        
        # Classify the text
        result = classifier(text, candidate_labels=categories)
        predicted_category = result['labels'][0]
        confidence_score = result['scores'][0]

        return {
            "detected_language": language,
            "predicted_category": predicted_category,
            "confidence_score": confidence_score
        }
    except LangDetectException:
        logger.error("Language detection failed.")
        raise HTTPException(status_code=400, detail="Invalid input text")
    except Exception as e:
        logger.error(f"Classification failed: {e}")
        raise HTTPException(status_code=500, detail="Classification failed")

