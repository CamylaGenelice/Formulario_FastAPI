from fastapi import APIRouter, HTTPException
from src.schemas.schemas import CreateProduct
from src.service.product_service import CreateProduct
from src.service.product_service import ProductService

product_router = APIRouter(prefix="/prod", tags=["product"])

@product_router.post('/produtos')

def create(product: CreateProduct):

    try:
       
        new_product =  ProductService().create_product(product)


        return {
            'message': 'Produto cadastrado com sucesso',
            'produto': new_product
        }
    except ValueError as e:
        
        raise HTTPException(status_code=400, detail=str(e))
    
    except HTTPException as e:
        return HTTPException(500, detail='Erro interno no servidor')
    
@product_router.get('/produtos')
def get_product():
    try:
        return ProductService().get_product()
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    except HTTPException as e:
        return HTTPException(500, detail='Erro interno no servidor')