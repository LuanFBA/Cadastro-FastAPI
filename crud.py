from sqlalchemy.orm import Session

import models
import schemas


def obter_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

def listar_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def cadastrar_cliente(db: Session, cliente: schemas.Cliente):
    cli = models.Cliente(**cliente.dict())
    db.add(cli)
    db.commit()
    db.refresh(cli)
    return cli

def remover_cliente(db: Session, cliente_id:int):
    cli = obter_cliente(db=db, cliente_id=cliente_id)
    db.delete(cli)
    db.commit()
