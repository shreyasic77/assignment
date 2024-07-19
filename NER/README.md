# FastAPI Named Entity Recognition (NER) and Database Integration

This project is a FastAPI application that performs Named Entity Recognition (NER) on input text and stores the results in a SQLite database. It includes API endpoints for performing NER and retrieving stored entities. Alembic is used for managing database schema migrations.

## Features

- **NER Endpoint**: Processes text to extract named entities and stores them in a SQLite database.
- **Retrieve Entities**: Fetches stored entities from the database based on entity type.
- **Database Migrations**: Uses Alembic for managing schema changes and migrations.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- spaCy
- SQLAlchemy
- Alembic
- SQLite 

# install dependencies
pip install -r requirements.txt

## Download spacy language model for NER
python -m spacy download en_core_web_lg


# configuring the database, by updating the alembic.ini file

sqlalchemy.url = sqlite:///./test.db

# Run the app
uvicorn main:app --reload

Open your browser and navigate to http://127.0.0.1:8000/docs to interact with the API endpoints.
