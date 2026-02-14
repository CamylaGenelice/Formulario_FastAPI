from fastapi import APIRouter, HTTPException
from src.schemas.schemas import CreateProduct
from src.service.product_service import CreateProduct

product_router = APIRouter(prefix="/orders", tags=["auth"])

@product_router.post('/produtos')

async def create(product: CreateProduct):

    try:
        new_product = CreateProduct(code=product.code, name=product.name, size=product.size)


        return {
            'message': 'Produo cadastrado com sucesso',
            'produto': new_product
        }
    except ValueError as e:
        
        raise HTTPException(status_code=400, detail=str(e))
    
    except HTTPException as e:
        return HTTPException(500, detail='Erro interno no servidor')
   