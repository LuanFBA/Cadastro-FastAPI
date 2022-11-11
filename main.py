from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"mensagem": "Hello world"}

@app.get("/api/v1/clientes", response_model=list[schemas.Cliente])
def listar_clientes(db: Session=Depends(get_db), skip: int = 0, limit: int = 100):
    clientes = crud.listar_clientes(db, skip=skip, limit=limit)
    return clientes

@app.get("/api/v1/clientes/{cliente_id}")
def obter_cliente(cliente_id: int, db: Session=Depends(get_db)):
    cliente = crud.obter_cliente(db=db, cliente_id=cliente_id)
    if cliente is not None:
        return cliente
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Cliente com id: {cliente_id} não existe"
    )

@app.post("/api/v1/clientes", response_model=schemas.Cliente, status_code=status.HTTP_201_CREATED)
def cadastrar_cliente(cliente: schemas.ClienteCreate, db:Session=Depends(get_db)):
    return crud.cadastrar_cliente(db=db, cliente=cliente)

@app.delete("/api/v1/clientes/{cliente_id}")
def remover_cliente(cliente_id: int ,db: Session=Depends(get_db)):
    cliente = crud.obter_cliente(db=db, cliente_id=cliente_id)
    if cliente is not None:
        return crud.remover_cliente(db=db, cliente_id=cliente_id)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Cliente com id: {cliente_id} não existe"
    )
