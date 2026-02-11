import sqlite3
from src.schemas.schemas import UsuarioCreate

class DataBase:

  def __init__(self, name='database.db'):
    
    self.name = name
    self._create_table()


  def _connect(self):
        # Criamos uma nova conexão a cada chamada para ser seguro com o FastAPI
        connection = sqlite3.connect(self.name)
        connection.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
        return connection

  def _create_table(self):
        with self._connect() as connect:
            connect.execute('''CREATE TABLE IF NOT EXISTS usuarios 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, senha TEXT)''')

  def create_users(self, usuario: UsuarioCreate):
        with self._connect() as connect:
            cursor = connect.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email,senha) VALUES (?, ?, ?)", 
                           (usuario.nome, usuario.email, usuario.senha,))
            connect.commit()
            return cursor.lastrowid

  def search(self, email: str):
        with self._connect() as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
            # Converte as linhas do banco em dicionários para o Pydantic entender
            return [dict(row) for row in cursor.fetchall()]