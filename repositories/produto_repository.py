# repositories/produto_repository.py

from models.produto_model import Produto

class ProdutoRepository:

    def __init__(self, db):
        self.db = db

    def save(self, produto_data):
        produto = Produto(**produto_data.dict())

        self.db.add(produto)
        self.db.commit()
        self.db.refresh(produto)

        return produto


    def update(self, produto_id, produto_data):

        produto = self.db.query(Produto).get(produto_id)

        if not produto:
            return None

        data = produto_data.model_dump(exclude_unset=True)

        for key, value in data.items():
            setattr(produto, key, value)

        self.db.add(produto)
        self.db.commit()
        self.db.refresh(produto)

        return produto

    def delete(self, produto_id):

        produto = self.db.query(Produto).get(produto_id)

        if not produto:
            return None

        self.db.delete(produto)
        self.db.commit()

        return True

    def get_by_id(self, produto_id):

        produto = self.db.query(Produto).get(produto_id)
        if not produto:
            return None

        return produto

    def get_all(self):
        return self.db.query(Produto).all()