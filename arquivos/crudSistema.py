from classCliente import Cliente
from classMaterial import Material
from classVenda import Venda
from classFuncionarios import Funcionario
import mysql.connector

#Conectamos o python com banco de dados
def iniciarConexao():
    #Talvez eu deva tirar esse try
    while True:
        try:
            conexao = mysql.connector.connect(
            host='localhost', 
            database='materialconstrucao', 
            user='root', 
            password='**'
            )
            return conexao
        except:
            raise ValueError("Conexão não estabelecida.")

#Inserindo colaborador na base de dados
def funcionario(colaborador):

    #Criando a uma conexao
    conexao = iniciarConexao()

    # Criação do cursor
    cursor = conexao.cursor()
    
    while True:
        try:
            colaborador = Funcionario(input("Insira seu nome: "),
                input("Insira seu endereco: "), 
                input("Insira seu e-mail: "),
                input("Insira seu cpf: "), 
                int(input("Insira seu telefone: "))
            )
            #Sair do loop caso dê certo
            break
        except ValueError:
            print("Insira apenas números para telefone.")
        
    #Verificando se existe colaborador na base de dados
    comando_select = f'SELECT cpf_cola FROM table_colaborador WHERE cpf_cola = "{colaborador.cpf}"'
    cursor.execute(comando_select)
    result = cursor.fetchone()

    if result:
        print("Colaborador já existente na base de dados.")
    else:
        comando = f'INSERT INTO table_colaborador (nome_cola,endereco_cola,email_cola,cpf_cola,telefone_cola,user_cola,senha_cola) VALUES\
        ("{colaborador.nome}", "{colaborador._endereco}", "{colaborador.email}", "{colaborador.cpf}", {colaborador.telefone},"{colaborador.usuario}","{colaborador.senha}")'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Atualiza o banco de dados
        conexao.commit()
        print("Ação realizada com sucesso.")
        cursor.close()
        conexao.close()

#Inserindo cliente na base de dados
def cliente(cliente):

    #Criando a uma conexao 
    conexao = iniciarConexao()

    # Criação do cursor
    cursor = conexao.cursor()
    while True:
        try:
            cliente = Cliente(input("Insira seu nome: "),
                input("Insira seu endereco: "), 
                input("Insira seu e-mail: "),
                input("Insira seu cpf: "), 
                int(input("Insira seu telefone: "))
            )
            #Sair do loop caso dê certo
            break
        except ValueError:
            print("Preencha apenas números para o telefone")

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
        cursor.close()
        conexao.close()
        
#Inserindo venda na base de dados
def venda(venda):

    #Criando a uma conexao 
    conexao = iniciarConexao()

    # Criação do cursor
    cursor = conexao.cursor()
    while True:
        try:
            venda = Venda(input("Valor Total: "))
        except:
            raise ValueError('Insira apenas numeros')
        
    #Inserindo uma venda na base de dados
    comando = f'INSERT INTO table_vendas (data_vendas,valorTotal_vendas) VALUES\
    ("{venda._data}", {venda._valorTotal})'
    #Executa o comando na base de dados 
    cursor.execute(comando)
    # Edita o banco de dados
    conexao.commit()
    #Atualiza o banco de dados
    print("Ação realizada com sucesso.")
    cursor.close()
    conexao.close()

#Cancelando venda na base de dados
def cancelaVenda():
    #Criando a uma conexao 
    conexao = iniciarConexao()

    # Criação do cursor
    cursor = conexao.cursor()

    #Cancelando uma venda na base de dados
    nome_produto = input("Nome produto: ")

    comando = f'DELETE FROM table_vendas WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    # edita o banco de dados
    conexao.commit()
    #Atualiza o banco de dados
    print("Ação realizada com sucesso.")
    cursor.close()
    conexao.close()

#Consultando material na base de dados
def vizualizarVenda():
    #Criando a uma conexao 
    conexao = iniciarConexao()

    # Criação do cursor
    cursor = conexao.cursor()

    #Vizualizando uma venda na base de dados
    comando = f'SELECT * FROM table_vendas'
    cursor.execute(comando)
    # ler o banco de dados
    resultado = cursor.fetchall() 
    print(resultado)
    print("Ação realizada com sucesso.")
    cursor.close()
    conexao.close()

#Inserindo material na base de dados
def material(material):

    #Criando a uma conexao 
    conexao = iniciarConexao()

    # Criação do cursor
    cursor = conexao.cursor()
    while True:
        try:
            material = Material(input("Nome material: "),
                int(input("Quantidade: ")),
                float(input("Preço: ")),
                input("Especificação: "),
                input("Data de fabricação: "),
                input("Fornecedor: ")
            )
            #Sair do loop caso dê certo
            break
        except ValueError:
            print("Insira apenas valores numéricos para quantidade e preço.")
    
    #Inserindo uma material na base de dados
    comando_select = f'SELECT nome_material FROM table_material WHERE nome_material = "{material.nome}"'
    cursor.execute(comando_select)
    result = cursor.fetchone()

    if result:
        print("Cliente já existente na base de dados.")
    else:
        comando = f'INSERT INTO table_material (nome_material,quantidade_material,preco_material,especificacao_material,dataFabricacao_material,fornecedor_material) VALUES\
        ("{material.nome}", {material.quantidade}, {material.preco}, "{material.especificacao}", {material.datafabricacao}, "{material.fornecedor}")'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Edita o banco de dados
        conexao.commit()
        #Atualiza o banco de dados
        print("Ação realizada com sucesso.")

        cursor.close()
        conexao.close()

#Removendo funcionario na base de dados
def removerFuncionario():

        #Criando a uma conexao 
        conexao = iniciarConexao()

        # Criação do cursor
        cursor = conexao.cursor()

        #Cancelando uma venda na base de dados
        cpf_funcionario = input("Nome produto: ")

        comando = f'DELETE FROM table_colaborador WHERE cpf_cola = "{cpf_funcionario}"'
        cursor.execute(comando)
        # edita o banco de dados
        conexao.commit()
        #Atualiza o banco de dados
        print("Ação realizada com sucesso.")
        cursor.close()
        conexao.close()

#As credenciais de funcionario e adm serão realizadas para liberar o acesso
def verificarCredenciais(usuario):

    #Criando  uma conexao 
    conexao = iniciarConexao()
    # Criação do cursor
    cursor = conexao.cursor()
    #Verificando as credenciais no banco de dados
    comando_select = f'SELECT user_cola, senha_cola FROM table_colaborador WHERE user_cola = "{usuario.usuario} AND senha_cola = "{usuario.senha}"'
    cursor.execute(comando_select)
    # ler o banco de dados
    result = cursor.fetchall() 
    
    if result:
        print('Acesso liberado')
    else:
        print("Acesso negado.")

    cursor.close()
    conexao.close()

    return comando_select
