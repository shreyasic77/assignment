from fastapi.testclient import TestClient
from app.main import app
from app.nlp import extract_keywords

client = TestClient(app)

def test_extract_keywords():
    response = client.post("/extract_keywords", json={"text": "Python is great for machine learning"})
    assert response.status_code == 200
    assert "keywords" in response.json()
    assert isinstance(response.json()["keywords"], list)

def test_extract_keywords_logic():
    keywords = extract_keywords("Python is great for machine learning")
    assert "python" in keywords
    assert "machine" in keywords
    assert "learning" in keywords
