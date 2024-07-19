from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
import spacy

# Initialize FastAPI
app = FastAPI()

# Initialize SQLite database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define models
class Entity(Base):
    __tablename__ = "entities"

    id = Column(Integer, primary_key=True, index=True)
    entity_text = Column(String)
    entity_type = Column(String)
    original_text = Column(Text)

    def as_dict(self):
        return {
            "entity_text": self.entity_text,
            "entity_type": self.entity_type,
            "original_text": self.original_text
        }

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Load spaCy NLP model for Named Entity Recognition
nlp = spacy.load("en_core_web_lg")

# POST endpoint for NER and storing entities
class TextItem(BaseModel):
    text: str

@app.post("/ner/")
def perform_ner(text_item: TextItem, db: Session = Depends(get_db)):
    # Perform NER using spaCy
    doc = nlp(text_item.text)
    
    # Extract entities
    entities = []
    for ent in doc.ents:
        entity = Entity(
            entity_text=ent.text,
            entity_type=ent.label_,
            original_text=text_item.text
        )
        entities.append(entity)
    
    # Store entities in the database
    try:
        db.bulk_save_objects(entities)
        db.commit()
        # Return the entities for verification
        return {"message": "Entities stored successfully", "entities": [e.as_dict() for e in entities]}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

# GET endpoint to retrieve entities based on type
@app.get("/entities/")
def get_entities(entity_type: str = None, db: Session = Depends(get_db)):
    query = db.query(Entity)
    if entity_type:
        query = query.filter(Entity.entity_type == entity_type)
    return [e.as_dict() for e in query.all()]
