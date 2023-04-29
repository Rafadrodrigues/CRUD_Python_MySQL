import mysql.connector
#conectamos o python com banco de dados
con = mysql.connector.connect(host='localhost', database='name_bd', user='root', password='88554663')

if con.is_connected():
    db_info = con.get_server_info()
    print('Conectado ao servidor MySQL')
    #Curso serve para nosso código interagir com o BD 
    cursor = con.cursor()
    cursor.execute('Select Database();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados ',linha)

if con.is_connected():
    cursor.close()
    con.close()
    print('Conexão com MySql foi encerrada. ')

cursor = conexao.cursor()

# Comandos para o CRUD

cursor.close()

conexao.close()

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