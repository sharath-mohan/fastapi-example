from sqlalchemy import  String, Float, Column, Integer
from app.database import Base
from pydantic import BaseModel

class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

class ItemBase(BaseModel):
    name: str
    price: float