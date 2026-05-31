# services/produto_service.py
from fastapi import Depends
from sqlalchemy.orm import Session
from repositories.produto_repository import ProdutoRepository
from database.connection import get_db

class ProdutoService:

    def __init__(
        self,
        db: Session = Depends(get_db)
    ):
        self.repository = ProdutoRepository(db)

    def create(self, produto_data):
        return self.repository.save(produto_data)

    def update(self, produto_id, produto_data):
        return self.repository.update(produto_id, produto_data)

    def delete(self, produto_id):
        return self.repository.delete(produto_id)

    def get_by_id(self, produto_id):
        return self.repository.get_by_id(produto_id)

    def get_all(self):
        return self.repository.get_all()

