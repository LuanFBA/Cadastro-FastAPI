from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Cliente(BaseModel):
    id: Optional[UUID] = uuid4()
    nome: str = Field(min_length=3, max_length=20)
    sobrenome: Optional[str] = None
    cpf : str = Field(min_length=11, max_length=14)
    telefone: Optional[str] = None
    email: str = Field(min_length=7, max_length=100)

