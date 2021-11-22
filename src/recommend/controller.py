from fastapi import APIRouter

from src.recommend.service import getMovieByNameService, getMoviesByActorsService

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Get all recommendations"}

@router.get("/byMovie/")
async def getMovieByName(name: str):
    try:
        result = await getMovieByNameService(name)
        return {"message": name, "result": result}
    except:
        return {"message": "An unhandled exception occurred"}

@router.get("/byActor/")
async def getMoviesByActors(name: str):
    try:
        result = await getMoviesByActorsService(name)
        return {"message": name, "result": result}
    except:
        return {"message": "An unhandled exception occurred"}