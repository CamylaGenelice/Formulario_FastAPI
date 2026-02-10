from src.schemas.schemas import UsuarioCreate, SearchUsuario
from src.model.db import DataBase
import re

class Service:

    def create_user(self, dados: UsuarioCreate):

        default = re.compile(r'^[A-Za-zÀ-ÖØ-öø-ÿ]+(?: [A-Za-zÀ-ÖØ-öø-ÿ]+)*$')

        if self.search_user(dados.email):
            raise ValueError('Email já esta cadastrado')
        
        if not default.match(dados.nome):
            raise ValueError('Nome inválido')
        
        usuario = UsuarioCreate(nome=dados.nome, email=dados.email, senha=dados.senha)
        

        return DataBase().create_users(usuario)
    
    def search_user(self, email: str):
        
        default = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

        if not default.match(email):
            raise ValueError('Email inválido')
        
        return DataBase().search_user(email)

        

