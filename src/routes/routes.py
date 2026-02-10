from fastapi import FastAPI, HTTPException
from src.schemas.schemas import UsuarioCreate
from src.service.services import Service

app = FastAPI()

@app.post('/usuarios')

def create(usuario: UsuarioCreate):
    try:
        user = Service().create_user(usuario)
        return {
            'message': 'Usuario cadastrado com sucesso',
            'id': user
        }

    except HTTPException as e:
        return HTTPException(500, detail='Erro interno no servidor')