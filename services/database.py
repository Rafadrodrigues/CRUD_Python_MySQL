import mysql.connector
import os

# Configuração da conexão
try:
    #Criando a uma conexao
    conexao = mysql.connector.connect(
        host='localhost', 
        user='root', 
        password='88554663',
        database = 'MATERIALCONSTRUCAO',
        )
except:
    raise ValueError("Conexão não estabelecida.")
finally:
    os.system("cls")

# Criação do cursor
cursor = conexao.cursor()