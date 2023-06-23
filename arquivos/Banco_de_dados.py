from classCliente import Cliente
from classMaterial import Material
from classVenda import Venda
from classFuncionarios import Funcionario
from classLogin import Login
from time import sleep
from typing import TypeVar, List
import os
import mysql.connector

T = TypeVar('T')
#Conectamos o python com banco de dados
def criar_tabela():

    try:
        #Criando a uma conexao
        conexao = mysql.connector.connect(
            host='localhost', 
            user='root', 
            password='88554663'
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

    table_funcionario =  """
    CREATE TABLE FUNCIONARIO (
        IDFUNCIONARIO INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        cpf VARCHAR(15) NOT NULL,
        telefone VARCHAR(15) NOT NULL,
        cargo VARCHAR(30) NOT NULL,
        endereco VARCHAR(200),
    )
    """
    cursor.execute(table_funcionario)

    table_cliente =  """
    CREATE TABLE CLIENTE (
        IDCLIENTE INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        idade INT NOT NULL,
        cpf VARCHAR(15) NOT NULL,
        telefone VARCHAR(15) NOT NULL,
        endereco VARCHAR(200),
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

def inserir_na_bd(usuario:T):
        
    #Criando a uma conexao
    conexao = iniciar_conexao()
    # Criação do cursor
    cursor = conexao.cursor()
    #Verificando se existe colaborador na base de dados
    comando_select = f'SELECT cpf_cola FROM table_colaborador WHERE cpf_cola = "{colaborador.cpf}"'
    cursor.execute(comando_select)
    result = cursor.fetchone()

    if result:
        print("Funcionário já existente na base de dados.")
    else:
        comando = f'INSERT INTO table_colaborador (nome_cola,endereco_cola,email_cola,cpf_cola,telefone_cola,user_cola,senha_cola) VALUES\
        ("{colaborador.nome}", "{colaborador.endereco}", "{colaborador.email}", "{colaborador.cpf}", {colaborador.telefone},"{colaborador.usuario}","{colaborador.senha}")'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Atualiza o banco de dados
        conexao.commit()
        print("Ação realizada com sucesso.")
    cursor.close()
    conexao.close()
#Inserindo colaborador na base de dados
def funcionario(colaborador):

   
            #Sair do loop caso dê certo
            # try:
            #Criando a uma conexao
            conexao = iniciar_conexao()

            # Criação do cursor
            cursor = conexao.cursor()
            #Verificando se existe colaborador na base de dados
            comando_select = f'SELECT cpf_cola FROM table_colaborador WHERE cpf_cola = "{colaborador.cpf}"'
            cursor.execute(comando_select)
            result = cursor.fetchone()

            if result:
                print("Funcionário já existente na base de dados.")
            else:
                comando = f'INSERT INTO table_colaborador (nome_cola,endereco_cola,email_cola,cpf_cola,telefone_cola,user_cola,senha_cola) VALUES\
                ("{colaborador.nome}", "{colaborador.endereco}", "{colaborador.email}", "{colaborador.cpf}", {colaborador.telefone},"{colaborador.usuario}","{colaborador.senha}")'
                #Executa o comando na base de dados 
                cursor.execute(comando)
                # Atualiza o banco de dados
                conexao.commit()
                print("Ação realizada com sucesso.")
            cursor.close()
            conexao.close()

#Inserindo cliente na base de dados
def cliente(cliente):

    while True:
        #Eu poderia ter feito um isinstance para o numero de telefone, porém, optiei por deixar esse aqui
        try:
            cliente = Cliente(
                input("Insira seu nome: "),
                input("Insira seu endereco: "), 
                input("Insira seu e-mail: "),
                input("Insira seu cpf: "), 
                int(input("Insira seu telefone: ")),
                int(input("Número do cartão ")),
            )
            #Criando a uma conexao 
            conexao = iniciar_conexao()

            # Criação do cursor
            cursor = conexao.cursor()
            #Verificando se existe cliente na base de dados
            comando_select = f'SELECT cpf_cliente FROM table_cliente WHERE cpf_cliente = "{cliente.cpf}"'
            cursor.execute(comando_select)
            result = cursor.fetchone()

            if result:
                print("Cliente já existente na base de dados.")
            else:
                comando = f'INSERT INTO table_cliente (nome_cliente,endereco_cliente,email_cliente,cpf_cliente,telefone_cliente) VALUES\
                ("{cliente.nome}", "{cliente.endereco}", "{cliente.email}", "{cliente.cpf}", {cliente.telefone})'
                #Executa o comando na base de dados 
                cursor.execute(comando)
                # Edita o banco de dados
                conexao.commit()
                #Atualiza o banco de dados
                print("Ação realizada com sucesso.")
                #Sair do loop caso dê certo
                break

        except ValueError:
            print("Preencha apenas números para o telefone")
        except:
            print('Erro ao realizar o cadastro')
        finally:
            cursor.close()
            conexao.close()

#Inserindo venda na base de dados
def venda(venda):
    while True:
        try:
            venda = Venda(
                float(input("Valor Total da Venda: ")),
                input("Data da venda-(dd/mm/yy): "),
            )
            
            # Criando uma conexão
            conexao = iniciar_conexao()

            # Criação do cursor
            cursor = conexao.cursor()

            # Inserindo uma venda na base de dados
            comando = f'INSERT INTO table_vendas (valorTotal_vendas) VALUES ("{venda.valor_total}")'
            cursor.execute(comando)

            # Edita o banco de dados
            conexao.commit()

            # Atualiza o banco de dados
            print("Ação realizada com sucesso.")
            break
        except:
            print('Erro ao realizar venda. ')
        finally:
            cursor.close()
            conexao.close()

#Cancelando venda na base de dados
def cancela_venda():
    while True:
        try:
            #Criando a uma conexao 
            conexao = iniciar_conexao()

            # Criação do cursor
            cursor = conexao.cursor()

            #Cancelando uma venda na base de dados
            id_venda= input("Id da Venda: ")

            comando = f'DELETE FROM table_vendas WHERE id_vendas = "{id_venda}"'
            cursor.execute(comando)
            # edita o banco de dados
            conexao.commit()
            #Atualiza o banco de dados
            print("Ação realizada com sucesso.")
        except:
            print('Erro ao cancelar venda. ')
        finally:
            cursor.close()
            conexao.close()

#Consultando material na base de dados
def vizualizar_venda():
    #Para melhor vizualização, pode aprensentar informação com um dicionario
    while True:
        try:
            #Criando a uma conexao 
            conexao = iniciar_conexao()

            # Criação do cursor
            cursor = conexao.cursor()

            #Vizualizando uma venda na base de dados
            comando = f'SELECT * FROM table_vendas'
            cursor.execute(comando)
            # ler o banco de dados
            resultado = cursor.fetchall() 
            print(resultado)
            print("Ação realizada com sucesso.")
            break
        except:
            print("Erro ao consultar venda.")
        finally:
            cursor.close()
            conexao.close()

#Inserindo material na base de dados
def material(material):
    while True:
        try:
            material = Material(
                input("Nome material: "),
                int(input("Quantidade: ")),
                float(input("Preço: ")),
                input("Especificação: "),
                input("Data do material-(dd/mm/yy): "),
                input("Fornecedor: "),
            )

            #Criando a uma conexao 
            conexao = iniciar_conexao()

            # Criação do cursor
            cursor = conexao.cursor()
            
            #Inserindo uma material na base de dados
            comando_select = f'SELECT nome_material FROM table_material WHERE nome_material = "{material.nome}"'
            cursor.execute(comando_select)
            result = cursor.fetchone()

            if result:
                print("Material já existente na base de dados.")
            else:
                comando = f'INSERT INTO table_material (nome_material,quantidade_material,preco_material,especificacao_material,fornecedor_material) VALUES\
                ("{material.nome}", {material.quantidade}, {material.preco}, "{material.especificacao}",  "{material.fornecedor}")'
                #Executa o comando na base de dados 
                cursor.execute(comando)
                # Edita o banco de dados
                conexao.commit()
                #Atualiza o banco de dados
                print("Ação realizada com sucesso.")
                break
        except ValueError:
            print("Insira apenas valores numéricos para quantidade e preço.")
        except:
            print('Erro ao inserir material')
        finally:
            cursor.close()
            conexao.close()

#Removendo funcionario na base de dados
def remover_funcionario():

    try:
        #Criando a uma conexao 
        conexao = iniciar_conexao()

        # Criação do cursor
        cursor = conexao.cursor()

        #Cancelando uma venda na base de dados
        cpf_funcionario = input("Cpf do funcionário: ")

        comando = f'DELETE FROM table_colaborador WHERE cpf_cola = "{cpf_funcionario}"'
        cursor.execute(comando)
        # edita o banco de dados
        conexao.commit()
        #Atualiza o banco de dados
        print("Ação realizada com sucesso.")
    except:
        print('Erro ao remover colaborador')
    finally:
        cursor.close()
        conexao.close()

#As credenciais de funcionario e adm serão realizadas para liberar o acesso
def verificar_credenciais(login):

    login = Login(
            input('Insira seu usuário: '),
            input('Insira sua senha: '),
        )

    try:
        # Criando uma conexao 
        conexao = iniciar_conexao()

        # Criação do cursor
        cursor = conexao.cursor()

        # Verificando as credenciais no banco de dados
        comando_select = f'SELECT user_cola, senha_cola FROM table_colaborador WHERE user_cola = "{login.usuario}" AND senha_cola = "{login.senha}"'
        cursor.execute(comando_select)

        # Ler o banco de dados
        resultado = cursor.fetchall() 
        
        #Código inline
        if resultado:
            print('Acesso liberado')
            sleep(2)
            return True
        else:
            print('Acesso negado. Tente novamente')
            resposta = input("Deseja tentar novamente? (S/N): ")
            os.system("cls")
            if resposta.upper() == "N":
                quit()

    except Exception as e:
        print(f"Erro ao verificar credenciais: {str(e)}")
        return False
    
    finally:
        cursor.close()
        conexao.close()