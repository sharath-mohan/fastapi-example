from sqlalchemy import  String, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from pydantic import BaseModel
from  typing import List

class Item(Base):
    __tablename__ = "item"
    item_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), index=True)
    price: Mapped[float] = mapped_column(Float)
    category_id: Mapped[int] = mapped_column(ForeignKey("item_category.category_id"))

    category:Mapped["ItemCategory"] = relationship("ItemCategory", back_populates="item")
    

class ItemBase(BaseModel):
    name: str
    price: float
    category_id: int



class ItemCategory(Base):
    __tablename__ = "item_category"
    category_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category_name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    item: Mapped[List["Item"]] = relationship("Item", back_populates="category")