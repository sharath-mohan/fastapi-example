from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.routers import items
from app.database import get_db

origins = [
    "http://localhost:5123",
]


app = FastAPI(title="My API",)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"], 
    allow_headers=["*"],
)

get_db()

app.include_router(items.router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"Hello": "World"}
