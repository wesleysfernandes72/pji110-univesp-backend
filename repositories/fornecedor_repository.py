# repositories/fornecedor_repository.py

from models.fornecedor_model import Fornecedor

class FornecedorRepository:

    def __init__(self, db):
        self.db = db

    def save(self, fornecedor_data):
        fornecedor = Fornecedor(**fornecedor_data.dict())

        self.db.add(fornecedor)
        self.db.commit()
        self.db.refresh(fornecedor)

        return fornecedor


    def update(self, fornecedor_id, fornecedor_data):

        fornecedor = self.db.query(Fornecedor).get(fornecedor_id)

        if not fornecedor:
            return None

        data = fornecedor_data.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(fornecedor, key, value)

        self.db.add(fornecedor)
        self.db.commit()
        self.db.refresh(fornecedor)

        return fornecedor

    def delete(self, fornecedor_id):

        fornecedor = self.db.query(Fornecedor).get(fornecedor_id)

        if not fornecedor:
            return None

        self.db.delete(fornecedor)
        self.db.commit()

        return True

    def get_by_id(self, fornecedor_id):

        fornecedor = self.db.query(Fornecedor).get(fornecedor_id)
        if not fornecedor:
            return None

        return fornecedor

    def get_all(self):
        return self.db.query(Fornecedor).all()