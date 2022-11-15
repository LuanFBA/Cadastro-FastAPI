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

class UsuarioBase(BaseModel):
    nome: str
    email: str
    senha: str

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

class UsuarioDB(Usuario):
    hashed_senha: str

class LoginData(BaseModel):
    senha: str
    email: str

class LoginSucesso(BaseModel):
    usuario: Usuario
    access_token: str
