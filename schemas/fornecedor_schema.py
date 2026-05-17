# schemas/fornecedor_schemas.py

from pydantic import BaseModel

class FornecedorCreate(BaseModel):
    nome: str
    email: str
    telefone: str
    cnpj: str

class FornecedorUpdate(BaseModel):
    nome: str | None = None
    email: str | None = None
    telefone: str | None = None
    cnpj: str | None = None

class FornecedorResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str
    cnpj: str