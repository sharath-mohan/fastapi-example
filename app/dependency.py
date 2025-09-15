from typing import Optional, Annotated
from fastapi import Query
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends


class CommonQueryParams:
    def __init__(self, search: Optional[str] = None, limit:Annotated[int,Query(gt=0)] =10, offset: Annotated[int,Query(ge=0)] = 0):
        self.search = search
        self.limit = limit
        self.offset = offset

db_dependency = Annotated[Session, Depends(get_db)]