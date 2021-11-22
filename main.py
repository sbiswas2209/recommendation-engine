from fastapi import FastAPI
from src.server import router
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Movie Recommendation Engine API"}

app.include_router(router, prefix="/api")