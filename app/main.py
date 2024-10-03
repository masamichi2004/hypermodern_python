from fastapi import APIRouter, FastAPI
from app.middleware.cors import CorsConfig

app = FastAPI()
cors = CorsConfig(app)

cors.apply()

router = APIRouter()

@app.get("/")
async def root():
    return {"message": "Hello World"}