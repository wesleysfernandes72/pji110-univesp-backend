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