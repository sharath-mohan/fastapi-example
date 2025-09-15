from fastapi import FastAPI


from app.routers import items
from app.database import get_db



app = FastAPI(title="My API",)


get_db()

app.include_router(items.router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"Hello": "World"}
