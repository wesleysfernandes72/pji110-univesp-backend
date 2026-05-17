from fastapi import FastAPI

from database.base import Base
from database.connection import engine

from models.fornecedor_model import Fornecedor

from controllers.fornecedor_controller import router as fornecedor_router
app = FastAPI(
    title="PI UNIVESP",
    version="1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(fornecedor_router)


