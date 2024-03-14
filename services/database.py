import pymysql
import os

try:
    # Criando a conexão
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='88554663',
        database='materialconstrucao'
    )
except:
    raise ValueError("Conexão não estabelecida.")
finally:
    os.system("cls")

# Criação do cursor
cursor = conexao.cursor()