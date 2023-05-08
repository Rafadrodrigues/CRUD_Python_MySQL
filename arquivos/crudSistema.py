from classCliente import Cliente
from classMaterial import Material
from classVenda import Venda
from classFuncionarios import Funcionario
import mysql.connector

#Conectamos o python com banco de dados
def iniciarConexao():
    try:
        conexao = mysql.connector.connect(
        host='localhost', 
        database='materialconstrucao', 
        user='root', 
        password='88554663'
        )
        return conexao
    except:
        raise ValueError("Conexão não estabelecida.")

#Inserindo colaborador na base de dados
def colaborador(colaborador):

    #Criando a uma conexao

    conexao = iniciarConexao()

    # Criação do cursor
    cursor = conexao.cursor()

    colaborador = Funcionario(input("Insira seu nome: "),
        input("Insira seu endereco: "), 
        input("Insira seu e-mail: "),
        input("Insira seu cpf: "), 
        int(input("Insira seu telefone: "))
        )
    #Verificando se existe colaborador na base de dados
    comando_select = f'SELECT cpf_cola FROM table_colaborador WHERE cpf_cola = "{colaborador._cpf}"'
    cursor.execute(comando_select)
    result = cursor.fetchone()

    if result:
        print("Colaborador já existente na base de dados.")
    else:
        comando = f'INSERT INTO table_colaborador (nome_cola,endereco_cola,email_cola,cpf_cola,telefone) VALUES\
        ("{colaborador._nome}", "{colaborador._endereco}", "{colaborador._email}", "{colaborador._cpf}", {colaborador._telefone})'
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

    cliente = Cliente(input("Insira seu nome: "),
        input("Insira seu endereco: "), 
        input("Insira seu e-mail: "),
        input("Insira seu cpf: "), 
        int(input("Insira seu telefone: "))
        )

    #Verificando se existe cliente na base de dados
    comando_select = f'SELECT cpf_cliente FROM table_cliente WHERE cpf_cliente = "{cliente._cpf}"'
    cursor.execute(comando_select)
    result = cursor.fetchone()

    if result:
        print("Cliente já existente na base de dados.")
    else:
        comando = f'INSERT INTO table_cliente (nome_cliente,endereco_cliente,email_cliente,cpf_cliente,telefone_cliente) VALUES\
        ("{cliente._nome}", "{cliente._endereco}", "{cliente._email}", "{cliente._cpf}", {cliente._telefone})'
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
    venda = Venda(input("Valor Total: "))
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

    material = Material(input("Nome material: "),
        int(input("Quantidade: ")),
        float(input("Preço: ")),
        input("Especificação: "),
        input("Data de fabricação: "),
        input("Fornecedor: ")
        )
    
    #Inserindo uma material na base de dados
    comando_select = f'SELECT nome_material FROM table_material WHERE nome_material = "{material._nome}"'
    cursor.execute(comando_select)
    result = cursor.fetchone()

    if result:
        print("Cliente já existente na base de dados.")
    else:
        comando = f'INSERT INTO table_material (nome_material,quantidade_material,preco_material,especificacao_material,dataFabricacao_material,fornecedor_material) VALUES\
        ("{material._nome}", {material._quantidade}, {material._preco}, "{material._especificacao}", {material._datafabricacao}, "{material._fornecedor}")'
        #Executa o comando na base de dados 
        cursor.execute(comando)
        # Edita o banco de dados
        conexao.commit()
        #Atualiza o banco de dados
        print("Ação realizada com sucesso.")

        cursor.close()
        conexao.close()