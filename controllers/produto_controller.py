# controllers/produto_controller.py
from typing import List

from fastapi import APIRouter, Depends
from schemas.produto_schema import ProdutoCreate, ProdutoResponse, ProdutoUpdate
from services.produto_service import ProdutoService

router = APIRouter(prefix="/produto", tags=["Produto"])

@router.post("/", response_model=ProdutoResponse)
def create_produto(
        produto: ProdutoCreate,
        service: ProdutoService = Depends()
):
    return service.create(produto)

@router.put("/{produto_id}", response_model=ProdutoResponse)
def update_produto(
        produto_id: int,
        produto: ProdutoUpdate,
        services: ProdutoService = Depends()
):
    return services.update(produto_id, produto)

@router.delete("/{produto_id}", status_code=204)
def delete_produto(
        produto_id: int,
        services: ProdutoService = Depends()
):
    return services.delete(produto_id)

@router.get("/{produto_id}", response_model=ProdutoResponse)
def get_produto_by_id(
        produto_id: int,
        services:ProdutoService = Depends()
):
    return services.get_by_id(produto_id)

@router.get("/", response_model=List[ProdutoResponse])
def get_all(
        services: ProdutoService = Depends()
):
    return services.get_all()