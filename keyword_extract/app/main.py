from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from . import models, schemas, crud, database, nlp
from .database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/extract_keywords", response_model=schemas.KeywordResponse)
async def extract_keywords(text_data: schemas.TextData, db: Session = Depends(get_db)):
    keywords = nlp.extract_keywords(text_data.text)
    crud.save_keywords(db, keywords)
    return {"keywords": keywords}

@app.get("/trending_topics")
async def trending_topics(top_n: int = 10, days: int = 7, db: Session = Depends(get_db)):
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=days)
    keywords = crud.get_trending_keywords(db, top_n, start_date, end_date)
    return {"trending_topics": keywords}
