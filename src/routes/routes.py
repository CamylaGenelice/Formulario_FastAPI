from fastapi import APIRouter, HTTPException
from src.schemas.schemas import UsuarioCreate
from src.service.services import UserService



auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post('/usuarios')
def create(usuario: UsuarioCreate):
    try:
        user = UserService().create_user(usuario)
        return {
            'message': 'Usuario cadastrado com sucesso',
            'id': user
        }
    except ValueError as e:
        
        raise HTTPException(status_code=400, detail=str(e))
    
    except HTTPException as e:
        return HTTPException(500, detail='Erro interno no servidor')