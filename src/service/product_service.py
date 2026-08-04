from src.schemas.schemas import CreateProduct
from src.model.product_model import DataProduct

class ProductService:

    def create_product(self, product: CreateProduct):
        try:
            # remove os espaços
            product.code = product.code.replace(" ", "")

            if  self.search_product(product.code):
                raise ValueError('Produto já esta cadastrado')
            
            
            obj = DataProduct()
            return obj.create_product(product)
        
            

        except Exception as e:
            print('Erro: ',e)
            raise ValueError('Erro ao criar produto')

    def search_product(self, code:str ):
        try:
            

             return DataProduct().search_product(code)
        
        except Exception as e:
            print('Erro: ',e)
            raise ValueError('Erro ao buscar produto')
        
    def get_product(self):
        try:
            return DataProduct().get_product()
        except Exception as e:
            print('Erro: ',e)
            raise ValueError('Erro ao buscar produto')