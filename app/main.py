from fastapi import FastAPI
from app.infra.api.router import router as api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/", status_code=200)
def index():
    return {"message":"БЭК ЖИВ"}