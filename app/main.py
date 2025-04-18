from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.infra.api.router import router as api_router
from app.infra.database.init_db import seed_demo_data, create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    seed_demo_data()
    yield

app = FastAPI(title="EchoBudget", lifespan=lifespan)

app.include_router(api_router)

@app.get("/", status_code=200)
def index():
    return {"message":"БЭК ЖИВ"}
