from pydantic import BaseModel, EmailStr
from typing import Optional


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class SearchUsuario(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True
class UsuarioResponse(BaseModel):

    id: int
    class Config:
        from_attributes = True