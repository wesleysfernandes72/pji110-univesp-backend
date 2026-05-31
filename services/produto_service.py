# services/produto_service.py

from repositories.produto_repository import ProdutoRepository
from database.connection import SessionLocal

class ProdutoService:

    def __init__(self):
        db = SessionLocal()
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

