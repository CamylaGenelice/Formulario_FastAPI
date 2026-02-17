import sqlite3
from src.schemas.schemas import CreateProduct, ProductResponse

class DataProduct:

    def __init__(self, name='product.db'):
        self.name = name
        self._create_table()

    def _connect(self):
        connection = sqlite3.connect(self.name)
        connection.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
        return connection
    
    def _create_table(self):
        try:
            with self._connect() as connect:
                connect.execute('''CREATE TABLE IF NOT EXISTS produto 
                              (id INTEGER PRIMARY KEY AUTOINCREMENT, code TEXT, name TEXT, size TEXT)''')
                connect.commit()
        except Exception as e:
            print('ERRO: ', e)
    
    def create_product(self, product: CreateProduct) :
        try:
            with self._connect() as connect:
                cursor = connect.cursor()
                cursor.execute("INSERT INTO produto (code, name, size) VALUES (?,?,?)", (product.code, product.name, product.size,))

            connect.commit()
            return product
        
        except Exception as e:
            print('ERRO: ', e)
            raise e

    def search_product(self, code: str):
        try:
         with self._connect() as connect:
            cursor = connect.cursor()  
            cursor.execute("SELECT * FROM produto WHERE code = ?",(code,)) 
            return [dict(row) for row in cursor.fetchall()]
         
        except Exception as e:
            print('ERRO: ', e)
            raise e

    def get_product(self):
       with self._connect() as connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM produto")
            return [dict(row) for row in cursor.fetchall()]
       
db = DataProduct('product.db')