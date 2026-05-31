# controllers/fornecedor_controller.py
from typing import List

from fastapi import APIRouter, Depends
from schemas.fornecedor_schema import FornecedorCreate, FornecedorResponse, FornecedorUpdate
from services.fornecedor_service import FornecedorService

router = APIRouter(prefix="/fornecedor", tags=["Fornecedor"])

@router.post("/", response_model=FornecedorResponse)
def create_fornecedor(
        fornecedor: FornecedorCreate,
        service: FornecedorService = Depends()
):
    return service.create(fornecedor)

@router.put("/{fornecedor_id}", response_model=FornecedorResponse)
def update_fornecedor(
        fornecedor_id: int,
        fornecedor: FornecedorUpdate,
        services: FornecedorService = Depends()
):
    return services.update(fornecedor_id, fornecedor)

@router.delete("/{fornecedor_id}", status_code=204)
def delete_fornecedor(
        fornecedor_id: int,
        services: FornecedorService = Depends()
):
    return services.delete(fornecedor_id)

@router.get("/{fornecedor_id}", response_model=FornecedorResponse)
def get_fornecedor_by_id(
        fornecedor_id: int,
        services:FornecedorService = Depends()
):
    return services.get_by_id(fornecedor_id)

@router.get("/", response_model=List[FornecedorResponse])
def get_all(
        services: FornecedorService = Depends()
):
    return services.get_all()