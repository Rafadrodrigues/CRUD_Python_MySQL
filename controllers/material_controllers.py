import services.database as db
import models.material as material

def inserir(material):
    comando = f'INSERT INTO MATERIAL (nome, valor) VALUES \
    ("{material.nome}", {material.valor})'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()
 
def selecionar_todos_clientes():
    db.cursor.execute('SELECT * FROM MATERIAL')
    lista_de_material = []
    #Recuperando os itens que recuperamos em cima
    for linha in db.cursor.fetchall():
        lista_de_material.append(material.Material(linha[0],linha[1],linha[2]))
    
    return lista_de_material

def selecionar_id(id:str):
    db.cursor.execute(f'SELECT * FROM MATERIAL WHERE IDMATERIAL="{id}"')
    lista_de_material = []
    #Recuperando os itens que recuperamos em cima
    for linha in db.cursor.fetchall():
        lista_de_material.append(material.Material(linha[0],linha[1],linha[2]))
    
    #Como estou alterando apenas um cliente o retorno é apenas de um cliente
    return lista_de_material[0]

def excluir(id:str):
    comando = f'DELETE FROM MATERIAL WHERE IDMATERIAL = "{id}"'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()


def alterar(material):
    comando = f'UPDATE MATERIAL SET nome="{material.nome}", valor={material.valor} WHERE IDMATERIAL = "{material.id}"'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()
 
