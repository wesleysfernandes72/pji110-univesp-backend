# services/fornecedor_service.py
from fastapi import Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from repositories.fornecedor_repository import FornecedorRepository

class FornecedorService:

    def __init__(
            self,
            db: Session = Depends(get_db)
    ):
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

