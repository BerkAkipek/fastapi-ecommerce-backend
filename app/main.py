from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.api.router import api_router
from app.core.config import settings
from app.db.database import engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    print("Trying to connect the DB.")

    try:
        async with engine.begin() as connection:
            await connection.execute(text("SELECT 1"))
        print(f"DB connected at: {settings.DATABASE_URL}")
    except Exception as e:
        print(f"DB connection is failed with: \n{e}")
        raise
    yield
    await engine.dispose()
    print("DB connaction pool closed.")


app = FastAPI(
    title="Shopease", description="Shopease is an e-commerce API.", version="1.0.0", lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix="/api")
