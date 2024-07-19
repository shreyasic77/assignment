# Multilingual Text Classification API

This FastAPI project provides an endpoint for multilingual text classification. The API accepts text input in multiple languages, detects the language, translates the text to English if necessary, classifies it into predefined categories, and returns the detected language, translated text, predicted category, and confidence score.

## Features

- **Multilingual Support**: Accepts text in English, Spanish, and French.
- **Language Detection**: Automatically detects the language of the input text.
- **Text Translation**: Translates text to English if it's not already in English.
- **Text Classification**: Classifies the text into categories such as news, sports, entertainment, and technology.
- **Error Handling**: Provides proper error handling for unsupported languages and invalid inputs.

## Prerequisites

- Python 3.7 or later

# creating virtual environment and installing dependencies
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt


# Run the app
uvicorn main:app --reload

Open your browser and navigate to http://127.0.0.1:8000/docs to interact with the API endpoints.

We can test the API with curl, Postman, or any HTTP client to make POST requests to the /classify/ endpoint.


