import os
import mysql.connector

#Conectamos o python com banco de dados e criamos o banco de dados e suas tabelas
def criar_base():
    try:
        #Criando a uma conexao
        conexao = mysql.connector.connect(
            host='localhost', 
            user='root', 
            password='**',
            )
    except:
        raise ValueError("Conexão não estabelecida.")
    finally:
        os.system("cls")

    # Criação do cursor
    cursor = conexao.cursor()

    create_db = 'CREATE DATABASE MATERIALCONSTRUCAO'
    cursor.execute(create_db)
    print('Base criada com sucesso!')

#Com essa função vamos fazer as manipulações no banco de dados, talvez ela possa ser utilizada mais em cima 
def iniciar_conexao():
    
    try:
        #Criando a uma conexao
        conexao = mysql.connector.connect(
            host='localhost', 
            user='root', 
            password='**',
            database = 'MATERIALCONSTRUCAO',
            )
        return conexao
    except:
        raise ValueError("Conexão não estabelecida.")
    finally:
        os.system("cls")

def criar_tabelas():

    #Criando a uma conexao
    conexao = iniciar_conexao()
    # Criação do cursor
    cursor = conexao.cursor()
    
    table_funcionario =  """
    CREATE TABLE FUNCIONARIO (
        IDFUNCIONARIO INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        cpf VARCHAR(15) NOT NULL UNIQUE,
        telefone VARCHAR(15) NOT NULL,
        cargo VARCHAR(30) NOT NULL,
        endereco VARCHAR(200)
    )
    """
    cursor.execute(table_funcionario)

    table_cliente =  """
    CREATE TABLE CLIENTE (
        IDCLIENTE INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        cpf VARCHAR(15) NOT NULL UNIQUE,
        telefone VARCHAR(15) NOT NULL,
        endereco VARCHAR(200)
    )
    """
    cursor.execute(table_cliente)
    
    table_material =  """
    CREATE TABLE MATERIAL (
        IDMATERIAL INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        valor FLOAT(10,2) NOT NULL,
        data_hora VARCHAR(20) NOT NULL
    )
    """
    cursor.execute(table_material)

    table_venda =  """
        CREATE TABLE VENDA (
            IDVENDA INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(100) NOT NULL,
            quantidade INT NOT NULL,
            valor FLOAT(10,2) NOT NULL
        )
        """
    cursor.execute(table_venda)
    cursor.close()
    conexao.close()
    
#Uma função generica, porque ela realiza inserção da base de dados de todos tipo disponível no programa
def inserir_na_bd(selec_table,usuario:dict):
    #Criando a uma conexao
    conexao = iniciar_conexao()
    # Criação do cursor
    cursor = conexao.cursor()

    #Realizando inserção dos dados do funcionario na base de dados
    if 'Funcionário' in selec_table:
        comando = f'INSERT INTO FUNCIONARIO (nome, idade, cpf, telefone, cargo, endereco) VALUES \
        ("{usuario["nome"]}", {usuario["idade"]}, "{usuario["cpf"]}", "{usuario["telefone"]}", "{usuario["cargo"]}", "{usuario["endereco"]}")'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Atualiza o banco de dados
        conexao.commit()
        print("Funcionário adicionado com sucesso.")

    #Realizando inserção dos dados do Cliente na base de dados
    if 'Cliente' in selec_table:
        comando = f'INSERT INTO CLIENTE (nome, idade, cpf, telefone, endereco) VALUES \
        ("{usuario["nome"]}", {usuario["idade"]}, "{usuario["cpf"]}", "{usuario["telefone"]}", "{usuario["endereco"]}")'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Atualiza o banco de dados
        conexao.commit()
        print("Cliente adicionado com sucesso.")

    #Realizando inserção dos dados do Material na base de dados
    if 'Material' in selec_table:
        comando = f'INSERT INTO MATERIAL (nome,data_hora,valor) VALUES\
        ("{usuario["nome"]}", "{usuario["data"]}",{usuario["valor"]})'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Atualiza o banco de dados
        conexao.commit()
        print("Material adicionado com sucesso.")

    #Realizando inserção dos dados da Venda na base de dados
    if 'Venda' in selec_table:
        comando = f'INSERT INTO VENDA (nome,valor,quantidade) VALUES\
        ("{usuario["nome"]}", {usuario["valor"]}, {usuario["quantidade"]})'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Atualiza o banco de dados
        conexao.commit()
        print("Venda adicionada com sucesso.")
        
    cursor.close()
    conexao.close()

#Cancelando venda na base de dados
def deletar_na_bd(selec_table:str, id:str):

    #Criando a uma conexao
    conexao = iniciar_conexao()
    # Criação do cursor
    cursor = conexao.cursor()

    #Realizando remoção do funcionario na base de dados
    if 'Funcionário' in selec_table:
        comando = f'DELETE FROM FUNCIONARIO WHERE CPF = "{id}"'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Atualiza o banco de dados
        conexao.commit()
        print("Funcionário removido com sucesso.")

    #Realizando a remoção do cliente na base de dados
    if 'Cliente' in selec_table :
        comando = f'DELETE FROM CLIENTE WHERE CPF = "{id}"'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Atualiza o banco de dados
        conexao.commit()
        print("Cliente removido com sucesso.")

    #Realizando a remoção do cliente na base de dados
    if 'Material' in selec_table:
        comando = f'DELETE FROM Material WHERE NOME = "{id}"'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Atualiza o banco de dados
        conexao.commit()
        print("Material removido com sucesso.")

    #Realizando a remoção do cliente na base de dados
    if 'Venda' in selec_table:
        comando = f'DELETE FROM VENDA WHERE NOME = "{id}"'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Atualiza o banco de dados
        conexao.commit()
        print("Venda removido com sucesso.")

    cursor.close()
    conexao.close()

#Consultando material na base de dados
def vizualizar_na_bd(selec_table:str):
        
    #Para melhor vizualização, pode aprensentar informação com um dicionario
        #Criando a uma conexao 
        conexao = iniciar_conexao()
        # Criação do cursor
        cursor = conexao.cursor()

        #Vizualizando informações do funcionario na base de dados
        if 'Funcionário' in selec_table:
            comando = f'SELECT * FROM FUNCIONARIO'
            #Executa o comando na base de dados 
            cursor.execute(comando)
            # ler o banco de dados
            resultado = cursor.fetchall()
            print(resultado)
            # Atualiza o banco de dados
            conexao.commit()
            print("Ação realizada com sucesso.")
        
        #Vizualizando informações do cliente na base de dados
        if 'Cliente' in selec_table:
            comando = f'SELECT * FROM CLIENTE'
            #Executa o comando na base de dados 
            cursor.execute(comando)
            # ler o banco de dados
            resultado = cursor.fetchall()
            print(resultado)
            # Atualiza o banco de dados
            conexao.commit()
            print("Ação realizada com sucesso.")
        
        #Vizualizando informações do material na base de dados
        if 'Material' in selec_table:
            comando = f'SELECT * FROM Material'
            #Executa o comando na base de dados 
            cursor.execute(comando)
            # ler o banco de dados
            resultado = cursor.fetchall()
            print(resultado)
            # Atualiza o banco de dados
            conexao.commit()
            print("Ação realizada com sucesso.")
        
        #Vizualizando informações da venda na base de dados
        if 'Venda' in selec_table:
            comando = f'SELECT * FROM VENDA'
            #Executa o comando na base de dados 
            cursor.execute(comando)
            # ler o banco de dados
            resultado = cursor.fetchall()
            print(resultado)
            # Atualiza o banco de dados
            conexao.commit()
            print("Ação realizada com sucesso.")

        cursor.close()
        conexao.close()
