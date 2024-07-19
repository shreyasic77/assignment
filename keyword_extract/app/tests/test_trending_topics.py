from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import Keyword

client = TestClient(app)

def test_trending_topics():
    db = SessionLocal()
    keyword = Keyword(keyword="python", frequency=10)
    db.add(keyword)
    db.commit()
    db.close()

    response = client.get("/trending_topics?top_n=5&days=7")
    assert response.status_code == 200
    assert "trending_topics" in response.json()
    assert isinstance(response.json()["trending_topics"], list)
    assert response.json()["trending_topics"][0]["keyword"] == "python"
