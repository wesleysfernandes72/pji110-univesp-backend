# models/fornecedor_model.py

from sqlalchemy import Column, Integer, String

from database.base import Base


class Fornecedor(Base):
    __tablename__ = 'fornecedor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    telefone = Column(String(255), nullable=False)
    cnpj = Column(String(255), nullable=False)