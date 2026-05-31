from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database.base import Base
from database.connection import engine

from models.fornecedor_model import Fornecedor

from controllers.fornecedor_controller import router as fornecedor_router
from controllers.produto_controller import router as produto_router
app = FastAPI(
    title="PI UNIVESP",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Front aqui
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(fornecedor_router)
app.include_router(produto_router)


