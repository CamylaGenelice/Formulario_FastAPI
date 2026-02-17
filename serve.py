#uvicorn serve:app --reload

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # Em produção, coloque o endereço do seu front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.routes.routes import auth_router 
from src.routes.products_routes import product_router 

app.include_router(auth_router)
app.include_router(product_router)


