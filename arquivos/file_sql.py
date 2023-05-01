#Classe que vai ser responsável por ligação ao banco de dados
import mysql.connector

#conectamos o python com banco de dados
conexao = mysql.connector.connect(host='localhost', database='materialconstrucao', user='root', password='**')
cursor = conexao.cursor()
cursor.close()
conexao.close()
