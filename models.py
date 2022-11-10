from sqlalchemy import Column, Integer, String

from database import Base


class Cliente(Base):
    __tablespace__ = "cliente"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    sobrenome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    telefone = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
