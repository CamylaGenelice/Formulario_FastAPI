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

from src.routes.routes import auth_router as routes

app.include_router(routes)


