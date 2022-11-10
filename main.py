from uuid import UUID

from fastapi import FastAPI, HTTPException

from models import Cliente, ClienteUpdate

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
    return {"mensagem": "Hello world"}

@app.get("/api/v1/clientes")
def listar_clientes():
    return db

@app.post("/api/v1/clientes")
def cadastrar_cliente(cliente: Cliente):
    db.append(cliente)
    return {"id": cliente.id}

@app.delete("/api/v1/clientes/{cliente_id}")
def remover_cliente(cliente_id: UUID):
    for cliente in db:
        if cliente.id == cliente_id:
            db.remove(cliente)
            return "Cliente removido"
    raise HTTPException(
        status_code=404,
        detail=f"Cliente com id: {cliente_id} não existe"
    )

@app.put("/api/v1/clientes/{cliente_id}")
def alterar_cliente(cliente_update: ClienteUpdate, cliente_id: UUID):
    for cliente in db:
        if cliente.id == cliente_id:
            if cliente_update.nome is not None:
                cliente.nome = cliente_update.nome
            if cliente_update.sobrenome is not None:
                cliente.sobrenome = cliente_update.sobrenome
            if cliente_update.cpf is not None:
                cliente.cpf = cliente_update.cpf
            if cliente_update.telefone is not None:
                cliente.telefone = cliente_update.telefone
            if cliente_update.email is not None:
                cliente.email = cliente_update.email
            return "Cliente alterado"
    raise HTTPException(
        status_code=404,
        detail=f"Cliente com id: {cliente_id} não existe"
    )
