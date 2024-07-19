from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

class Keyword(Base):
    __tablename__ = "keywords"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, index=True)
    frequency = Column(Integer, default=1)
    timestamp = Column(DateTime, default=func.now())
