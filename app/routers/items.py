from fastapi import APIRouter, HTTPException, Path, Depends
from typing import Annotated

from app.dependency import CommonQueryParams, db_dependency
from app import models

router = APIRouter(
    prefix="/items",
    tags=["Items"],
)


@router.get("/")
async def read_items(db:db_dependency, commons: Annotated[CommonQueryParams,   Depends(CommonQueryParams)]):
    result = db.query(models.Item).all()
    return result
   

@router.get("/{item_id}")
async def read_item(item_id:Annotated[int, Path(gt=0)], db: db_dependency):
    item = db.query(models.Item).filter(models.Item.item_id == item_id).first()
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.post("/")
async def create_item(item: models.ItemBase, db: db_dependency):
    db_item = models.Item(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"item": item, "message": "Item created successfully"}


# # ...existing code...

# from sqlalchemy.exc import SQLAlchemyError

# @router.get("/")
# async def read_items(db: db_dependency, commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
#     try:
#         result = db.query(models.Item).all()
#         if not result:
#             return {"items": [], "message": "No items found"}
#         return result
#     except SQLAlchemyError as e:
#         raise HTTPException(status_code=500, detail="Database error")

# @router.post("/")
# async def create_item(item: models.ItemBase, db: db_dependency):
#     db_item = models.Item(name=item.name, price=item.price)
#     try:
#         db.add(db_item)
#         db.commit()
#         db.refresh(db_item)
#         return {"item": db_item, "message": "Item created successfully"}
#     except SQLAlchemyError as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail="Failed to create item")
# # ...existing code...