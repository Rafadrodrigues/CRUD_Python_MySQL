import services.database as db
import models.vendas as vendas


def inserir(vendas):
    comando = f'INSERT INTO VENDA (nome, quantidade, valor) VALUES \
    ("{vendas.nome}", {vendas.quantidade}, {vendas.valor})'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()
 
def selecionar_todos_clientes():
    db.cursor.execute('SELECT * FROM VENDA')
    lista_de_vendas = []
    #Recuperando os itens que recuperamos em cima
    for linha in db.cursor.fetchall():
        lista_de_vendas.append(vendas.Venda(linha[0],linha[1],linha[2],linha[3]))
    
    return lista_de_vendas

def selecionar_id(id:str):
    db.cursor.execute(f'SELECT * FROM VENDA WHERE IDVENDA ="{id}"')
    lista_de_vendas = []
    #Recuperando os itens que recuperamos em cima
    for linha in db.cursor.fetchall():
        lista_de_vendas.append(vendas.Venda(linha[0],linha[1],linha[2],linha[3]))
    
    #Como estou alterando apenas um cliente o retorno é apenas de um cliente
    return lista_de_vendas[0]

def excluir(id:str):
    comando = f'DELETE FROM VENDA WHERE IDVENDA = "{id}"'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()


def alterar(vendas):
    comando = f'UPDATE VENDA SET nome="{vendas.nome}", quantidade={vendas.quantidade}, valor="{vendas.valor}" WHERE IDVENDA = "{vendas.id}"'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()
 
