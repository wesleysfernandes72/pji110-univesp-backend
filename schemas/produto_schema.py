# schemas/produto_schema.py

from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str

class ProdutoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str