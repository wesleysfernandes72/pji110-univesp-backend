# services/fornecedor_service.py

from repositories.fornecedor_repository import FornecedorRepository
from database.connection import SessionLocal

class FornecedorService:

    def __init__(self):
        db = SessionLocal()
        self.repository = FornecedorRepository(db)

    def create(self, fornecedor_data):
        return self.repository.save(fornecedor_data)

    def update(self, fornecedor_id, fornecedor_data):
        return self.repository.update(fornecedor_id, fornecedor_data)

    def delete(self, fornecedor_id):
        return self.repository.delete(fornecedor_id)

    def get_by_id(self, fornecedor_id):
        return self.repository.get_by_id(fornecedor_id)

    def get_all(self):
        return self.repository.get_all()

