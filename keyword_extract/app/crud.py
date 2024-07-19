from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from . import models

def save_keywords(db: Session, keywords: List[str]):
    for keyword in keywords:
        db_keyword = db.query(models.Keyword).filter(models.Keyword.keyword == keyword).first()
        if db_keyword:
            db_keyword.frequency += 1
        else:
            db_keyword = models.Keyword(keyword=keyword)
            db.add(db_keyword)
    db.commit()

def get_trending_keywords(db: Session, top_n: int, start_date: datetime, end_date: datetime):
    return db.query(models.Keyword) \
             .filter(models.Keyword.timestamp.between(start_date, end_date)) \
             .order_by(models.Keyword.frequency.desc()) \
             .limit(top_n) \
             .all()
