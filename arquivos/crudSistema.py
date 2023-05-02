from classColaboradores import Colaboradores
from classCliente import Cliente
from classMaterial import Material
from classVenda import Venda
import file_sql

#Inserindo colaborador na base de dados
def colaborador(Colaboradores):
    comando_select = f'SELECT cpf_cola FROM table_colaborador WHERE cpf_cola = "{Colaboradores.cpf}"'
    file_sql.cursor.execute(comando_select)
    result = file_sql.cursor.fetchone()

    if result:
            print("Cliente já existente na base de dados.")
    else:
        comando = f'INSERT INTO table_colaborador (nome_cola,endereco_cola,email_cola,cpf_cola,telefone_cola) VALUES\
        ("{Colaboradores.nome}", "{Colaboradores.endereco}", "{Colaboradores.email}", "{Colaboradores.cpf}", {Colaboradores.telefone})'
        #Executa o comando na base de dados 
        file_sql.cursor.execute(comando)
        file_sql.close()
        # Edita o banco de dados
        file_sql.conexao.commit()

#Inserindo cliente na base de dados
def cliente(Cliente):
    comando_select = f'SELECT cpf_cliente FROM table_cliente WHERE cpf_cliente = "{Cliente.cpf}"'
    file_sql.cursor.execute(comando_select)
    result = file_sql.cursor.fetchone()

    if result:
            print("Cliente já existente na base de dados.")
    else:
        comando = f'INSERT INTO table_cliente (nome_cliente,endereco_cliente,email_cliente,cpf_cliente,telefone_cliente) VALUES\
        ("{Cliente.nome}", "{Cliente.endereco}", "{Cliente.email}", "{Cliente.cpf}", {Cliente.telefone})'
        #Executa o comando na base de dados 
        file_sql.cursor.execute(comando)
        file_sql.close()
        # Edita o banco de dados
        file_sql.conexao.commit()

#Inserindo venda na base de dados
def venda(Venda):
    comando = f'INSERT INTO table_vendas (data_vendas,valorTotal_vendas) VALUES\
    ("{Venda.data}", {Venda.valorTotal})'
    #Executa o comando na base de dados 
    file_sql.cursor.execute(comando)
    file_sql.close()
    # Edita o banco de dados
    file_sql.conexao.commit()

#Cancelando venda na base de dados
def cancelaVenda():
    nome_produto = input("Nome produto: ")
    comando = f'DELETE FROM table_vendas WHERE nome_produto = "{nome_produto}"'
    file_sql.cursor.execute(comando)
    file_sql.close()
    # edita o banco de dados
    file_sql.conexao.commit()

#Consultando material na base de dados
def vizualizarVenda():
    comando = f'SELECT * FROM table_vendas'
    file_sql.cursor.execute(comando)
    # ler o banco de dados
    resultado = file_sql.cursor.fetchall() 
    file_sql.close()
    print(resultado)

#Inserindo material na base de dados
def material(Material):
    comando_select = f'SELECT nome_material FROM table_material WHERE nome_material = "{Material.nome}"'
    file_sql.cursor.execute(comando_select)
    result = file_sql.cursor.fetchone()

    if result:
        print("Cliente já existente na base de dados.")
    else:
        comando = f'INSERT INTO table_material (nome_material,quantidade_material,preco_material,especificacao_material,dataFabricacao_material,fornecedor_material) VALUES\
        ("{Material.nome}", {Material.quantidade}, {Material.preco}, "{Material.especificacao}", {Material.datafabricacao}, "{Material.fornecedor}")'
        #Executa o comando na base de dados 
        file_sql.cursor.execute(comando)
        file_sql.close()
        # Edita o banco de dados
        file_sql.conexao.commit() 
