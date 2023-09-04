import services.database as db
import models.cliente as cliente

def inserir(cliente):
    comando = f'INSERT INTO CLIENTE (nome, idade, cpf, telefone, endereco) VALUES \
    ("{cliente.nome}", {cliente.idade}, "{cliente.cpf}", "{cliente.telefone}", "{cliente.endereco}")'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()
 
def selecionar_todos_clientes():
    db.cursor.execute('SELECT * FROM CLIENTE')
    lista_de_clientes = []
    #Recuperando os itens que recuperamos em cima
    for linha in db.cursor.fetchall():
        lista_de_clientes.append(cliente.Cliente(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5]))
    
    return lista_de_clientes

def selecionar_id(id:str):
    db.cursor.execute(f'SELECT * FROM CLIENTE WHERE IDCLIENTE="{id}"')
    lista_de_clientes = []
    #Recuperando os itens que recuperamos em cima
    for linha in db.cursor.fetchall():
        lista_de_clientes.append(cliente.Cliente(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5]))
    
    #Como estou alterando apenas um cliente o retorno é apenas de um cliente
    return lista_de_clientes[0]

def excluir(id:str):
    comando = f'DELETE FROM CLIENTE WHERE IDCLIENTE = "{id}"'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()


def alterar(cliente):
    comando = f'UPDATE CLIENTE SET nome="{cliente.nome}", idade={cliente.idade}, cpf="{cliente.cpf}", telefone="{cliente.telefone}", endereco="{cliente.endereco}"WHERE IDCLIENTE = "{cliente.id}"'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()
 
