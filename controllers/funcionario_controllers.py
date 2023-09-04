import services.database as db
import models.funcionario as funcionario


def inserir(funcionario):
    comando = f'INSERT INTO FUNCIONARIO (nome, idade, cpf, telefone, cargo, endereco) VALUES \
    ("{funcionario.nome}", {funcionario.idade}, "{funcionario.cpf}", "{funcionario.telefone}","{funcionario.cargo}", "{funcionario.endereco}")'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()
 
def selecionar_todos_clientes():
    db.cursor.execute('SELECT * FROM FUNCIONARIO')
    lista_de_funcionarios = []
    #Recuperando os itens que recuperamos em cima
    for linha in db.cursor.fetchall():
        lista_de_funcionarios.append(funcionario.Funcionario(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6]))
    
    return lista_de_funcionarios

def selecionar_id(id:str):
    db.cursor.execute(f'SELECT * FROM FUNCIONARIO WHERE IDFUNCIONARIO="{id}"')
    lista_de_funcionarios = []
    #Recuperando os itens que recuperamos em cima
    for linha in db.cursor.fetchall():
        lista_de_funcionarios.append(funcionario.Funcionario(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6]))
    
    #Como estou alterando apenas um cliente o retorno é apenas de um cliente
    return lista_de_funcionarios[0]

def excluir(id:str):
    comando = f'DELETE FROM FUNCIONARIO WHERE IDFUNCIONARIO = "{id}"'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados
    db.conexao.commit()


def alterar(funcionario):
    comando = f'UPDATE FUNCIONARIO SET nome="{funcionario.nome}", idade={funcionario.idade}, cpf="{funcionario.cpf}", telefone="{funcionario.telefone}", cargo="{funcionario.cargo}", endereco="{funcionario.endereco}"WHERE IDFUNCIONARIO = "{funcionario.id}"'
    #Executa o comando na base de dados 
    db.cursor.execute(comando)
    # Atualiza o banco de dados