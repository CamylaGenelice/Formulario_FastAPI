from src.schemas.schemas import CreateProduct, SearchProduct
from src.model.db import DataBase

class ProductService:

    async def create_product(self, product: CreateProduct, code: SearchProduct):
        try:
            if await self.search_product(code=code):
                raise ValueError('Produto já esta cadastrado')
            
            new_product =  CreateProduct(code=product.code, name=product.name, size=product.size)

            return DataBase().create_product(new_product)

        except Exception as e:
            print('Erro: ',e)
            raise ValueError('Erro ao criar produto')

    async def search_product(self, code:SearchProduct ):
        try:
             consult = SearchProduct(code=code.code)

             return DataBase().search_product(consult)
        
        except Exception as e:
            print('Erro: ',e)
            raise ValueError('Erro ao buscar produto')