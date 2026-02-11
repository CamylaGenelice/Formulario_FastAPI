from src.schemas.schemas import UsuarioCreate
from src.model.db import DataBase
import bcrypt
import re

class Service:

    def _validation_name(self, name):

        default = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$")

        if bool(default.match(name)):
            return True
        
        return False
    
    def _validation_email(self, email):

        default = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

        if bool(default.match(email)):

            return True
        
        return False
    

    async def create_user(self, dados: UsuarioCreate):
        try:

            if len(dados.senha) <= 8:
                raise ValueError('A senha deve ter pelo menos 8 caracteres')

            if await self.search_user(dados.email):
                raise ValueError('Email já esta cadastrado')
            
            if self._validation_name(dados.nome) != True:
                raise ValueError('Nome inválido')
            
            senha_bytes = dados.senha.encode('utf-8')
            salt = bcrypt.gensalt(10)
            senha_hash = bcrypt.hashpw(senha_bytes,salt)
            
            usuario =  UsuarioCreate(nome=dados.nome, email=dados.email, senha=senha_hash.decode('utf-8'))
            

            return DataBase().create_users(usuario)
        
        except Exception as e:
            print('Erro no services ' ,e)
            raise e
        
    async def search_user(self, email: str):
        
        try:
            
            if self._validation_email(email) != True:
                raise ValueError('Email inválido')
            
            return DataBase().search(email)
        
        except Exception as e:
            print('Erro no services ' ,e)
            raise e

        

