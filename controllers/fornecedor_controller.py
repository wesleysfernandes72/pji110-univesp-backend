# controllers/fornecedor_controller.py

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