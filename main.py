import crud
import hash_provider
import models
import schemas
import token_provider
from database import SessionLocal, engine, get_db
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from utils import oauth2_scheme, obter_usuario_logado

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def root():
    return {"mensagem": "Hello world"}

@app.post("/api/v1/token")
def login(login_data: schemas.LoginData, db: Session = Depends(get_db)):
    senha = login_data.senha
    email = login_data.email
    usuario = crud.obter_usuario_por_email(db=db, usuario_email=email)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='E-mail ou senha estão incorretos!')
         
    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='E-mail ou senha estão incorretos!')
    # Gerar JWT
    token = token_provider.criar_access_token({'sub': usuario.email})
    return {"usuario": usuario, "access_token": token}
    
@app.post("/api/v1/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.Usuario)
def signup(usuario: schemas.UsuarioCreate, db: Session=Depends(get_db)):
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = crud.criar_usuario(db=db, usuario=usuario)
    return usuario_criado

@app.get("/api/v1/me")
def me(usuario: schemas.Usuario=Depends(obter_usuario_logado)):
    return usuario

@app.get("/api/v1/clientes", response_model=list[schemas.Cliente])
def listar_clientes(db: Session=Depends(get_db), token: str=Depends(oauth2_scheme), skip: int = 0, limit: int = 100):
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
