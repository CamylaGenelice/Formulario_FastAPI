# 🚀 Fórmulario de Cadastro API (FastAPI + SQLite)
Este é o back-end de um fórmulario simples, para aplicar os meus conhecimentos. Focado em Separação de Responsabilidades (SoC) e segurança na persistência de dados.

## 📋 Arquitetura do Projeto
O projeto foi estruturado seguindo padrões de camadas para facilitar a manutenção e escalabilidade:

* Models/DB (db.py): Camada de persistência que interage diretamente com o SQLite3. Utiliza RowFactory para mapeamento de dados.

* Services (services.py): Camada de lógica de negócio. Responsável por validações complexas (Regex), regras de senha e verificações de existência.

* Schemas (schemas.py): Contratos de dados utilizando Pydantic. Garante que a entrada e saída da API estejam sempre validadas.

* Routes (routes.py): Definição dos endpoints utilizando APIRouter, lidando com as requisições HTTP e exceções.

## 🛠️ Tecnologias Utilizadas
* Python 3.10+

* FastAPI: Framework web de alta performance.

* SQLite3: Banco de dados relacional leve.

* Pydantic: Validação de dados e Schemas.

* Regex (re): Validação de padrões de e-mail e nome.

## ⚙️ Funcionalidades e Regras de Negócio
Criação de Usuário:

* Valida se o e-mail já existe no banco antes de cadastrar.

* Verifica se o nome contém apenas caracteres válidos via Regex.

* Segurança: Impede o cadastro de senhas com menos de 8 caracteres.

## 🚀 Como Executar
1. Clone o repositório
   * git clone https://github.com/CamylaGenelice/Formulario_FastAPI.git
   
2. Crie um ambiente virtual:
```
  python -m venv venv
  source venv/bin/activate | No Windows: venv\Scripts\activate
```
3. Instale as dependências:
```pip install fastapi uvicorn pydantic```

4. Rode o servidor:
``` uvicorn main:app --reload```
