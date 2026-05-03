from sqlalchemy import Column, Integer, String
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)

from sqlalchemy import ForeignKey


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    status = Column(String)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))