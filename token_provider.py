from datetime import datetime, timedelta

from jose import jwt

SECRET_KEY = '80b170823b7814e1ed5ebae343eacb13fb8be76fbb6cb8a34cd769bd5939270b'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000

def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    dados.update({'exp': expiracao})
    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def verificar_access_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')
