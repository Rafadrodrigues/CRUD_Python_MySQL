import mysql.connector

#conectamos o python com banco de dados
conexao = mysql.connector.connect(host='localhost', database='materialconstrucao', user='root', password='88554663')

# if conexao.is_connected():
#     db_info = conexao.get_server_info()
#     print('Conectado ao servidor MySQL')
#     #Curso serve para nosso código interagir com o BD 
#     cursor = conexao.cursor()
#     cursor.execute('Select Database();')
#     linha = cursor.fetchone()
#     print('Conectado ao banco de dados ',linha)

# if conexao.is_connected():
#     cursor.close()
#     conexao.close()
#     print('Conexão com MySql foi encerrada. ')

cursor = conexao.cursor()
cursor.close()

conexao.close()
# Comandos para o CRUD

# CREATE
# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)

# UPDATE
# nome_produto = "todynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# DELETE
# nome_produto = "todynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados