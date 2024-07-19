from pydantic import BaseModel
from typing import List

class TextData(BaseModel):
    text: str

class KeywordResponse(BaseModel):
    keywords: List[str]
