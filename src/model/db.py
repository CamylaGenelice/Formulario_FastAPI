import sqlite3

class DataBase:

  def __init__(self,):
    
    self.connection = sqlite3.connect('database.db')
    self.cursor = self.connection.cursor()


    def _create_table(self):
      
      self.cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL,
                senha TEXT NOT NULL
            )
        '''
      )
      self.connection.commit()

    def insert_user(self, name, email, password):
      
      command = "INSERT INTO usuarios (nome, email, password) VALUES (?, ?)"
      self.cursor.execute(command, (name,email,password))
      self.connection.commit()

    def list_user(self):
      self.cursor.execute(
        "SELECT * FROM usuarios"
      )
      
      return self.cursor.fetchall()
    
    def search_user(self, email):
      
      self.cursor.execute(
        "SELECT * FROM usuarios WHERE email = ?",(email)
      )
      return self.cursor.fetchall()
    
    def close_connection(self):
      
      self.connection.close()
      print("Conexão encerrada")