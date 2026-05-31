# models/produto_model.py

from sqlalchemy import Column, Integer, String

from database.base import Base


class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)