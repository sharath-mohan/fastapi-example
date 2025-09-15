from sqlalchemy import  String, Float, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from pydantic import BaseModel

class Item(Base):
    __tablename__ = "items"
    item_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), index=True)
    price: Mapped[float] = mapped_column(Float)

class ItemBase(BaseModel):
    name: str
    price: float