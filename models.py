from database import Base
from sqlalchemy import Column, Integer, String


class Cliente(Base):
    __tablename__ = "cliente"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    sobrenome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    telefone = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
