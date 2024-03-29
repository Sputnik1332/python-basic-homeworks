from sqlalchemy import Column, Integer, String
from .database import db


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
