from pydantic import BaseModel


class ClienteBase(BaseModel):
    nome: str
    sobrenome: str
    cpf: str
    telefone: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True
