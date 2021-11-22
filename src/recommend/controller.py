from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Get all recommendations"}

@router.get("/movie/")
async def getMovieByName(name: str):
    return {"message": name}