# Keyword Extraction and Trending Topics System

This project is a system that performs keyword extraction on a stream of text data and identifies trending topics. It is built using FastAPI and leverages NLP techniques for keyword extraction. The system includes endpoints for extracting keywords and retrieving trending topics, stores data in a SQLite database, and uses GitHub Actions for CI/CD.

## Features

- FastAPI endpoint for keyword extraction from text data.
- TF-IDF technique for keyword extraction.
- Stores extracted keywords and their frequencies in a SQLite database.
- FastAPI endpoint for retrieving top N trending topics over a specified time range.
- CI/CD pipeline setup with GitHub Actions.
- Unit tests for keyword extraction and trending topics logic.

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- SQLAlchemy
- Scikit-learn
- Pytest

# virtual environment

python -m venv env
source env/bin/activate

# install dependencies
pip install -r requirements.txt

# launch the app
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000.

# Tests
pytest


