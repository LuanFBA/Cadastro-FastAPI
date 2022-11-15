import models
import schemas
from sqlalchemy.orm import Session


def obter_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

def listar_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def cadastrar_cliente(db: Session, cliente: schemas.Cliente):
    cliente = models.Cliente(**cliente.dict())
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

def remover_cliente(db: Session, cliente_id:int):
    cliente = obter_cliente(db=db, cliente_id=cliente_id)
    db.delete(cliente)
    db.commit()
    return "Cliente excluído com sucesso"

def criar_usuario(db: Session, usuario: schemas.Usuario):
    usuario = models.Usuario(**usuario.dict())
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def obter_usuario_por_email(db: Session, usuario_email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == usuario_email).first()
