import crud
import token_provider
from database import get_db
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from schemas import LoginData, Usuario
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def obter_usuario_logado(token: str=Depends(oauth2_scheme),
                         db: Session=Depends(get_db)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Token inválido")

    try:
        email: str = token_provider.verificar_access_token(token)
    except JWTError:
        raise exception

    if not email:
        raise exception
    usuario = crud.obter_usuario_por_email(db=db, usuario_email=email)

    if not usuario:
        raise exception

    return usuario
