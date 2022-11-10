from uuid import UUID

from fastapi import FastAPI

from models import Cliente

app = FastAPI()

db: list[Cliente] = [
    Cliente(
        id=UUID("a353965a-5e92-4b2b-9df8-77725f6c50d3"),
        nome="Luan",
        sobrenome="Felipe",
        cpf="111.222.333-44",
        telefone="(99)98877-6655",
        email="teste@teste.com"
        ),
    Cliente(
        id=UUID("2419b208-cb06-49cf-8b89-d452a08fd2d6"),
        nome="Marcell",
        sobrenome="Brilhante",
        cpf="111.222.333-55",
        telefone="(99)98877-7788",
        email="teste2@teste2.com"
        )
]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/api/v1/clientes")
def listar_clientes():
    return db

@app.post("/api/v1/clientes")
def cadastrar_cliente(cliente: Cliente):
    db.append(cliente)
    return {"id": cliente.id}
