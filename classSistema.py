from classColaboradores import Colaboradores
from classCliente import Cliente
from classMaterial import Material
import file_sql

#Classe referente analise realizada no banco de dados 
class Sistema(Colaboradores,Cliente):

    def __init__(self) -> None:
        self._colaboradores = []
        self._vendas=[]
        self._clientes=[]
        self._material=[]
    
    #Funcoes responsável por realizar atualizações na base de dados
    #incluindo colaborador na base de dados

    #Acho que vai ser preciso criar uma variavel como parametro cada método
    def incluirColaborador(self):
        #Inserindo colaborador na base de dados.
        #Preciso fazer uma condicional aqui para caso o colaborador já exista.
        comando = f'INSERT INTO table_colaborador (nome_cola,endereco_cola,email_cola,cpf_cola,telefone_cola) VALUES\
        ("{Colaboradores.nome}", "{Colaboradores.endereco}", "{Colaboradores.email}", "{Colaboradores.cpf}", {Colaboradores.telefone})'
        #Executa o comando na base de dados 
        file_sql.cursor.execute(comando)
        # Edita o banco de dados
        file_sql.conexao.commit() 

    def incluirCliente(self):
        #Inserindo cliente na base de dados
        #Preciso fazer uma condicional aqui para caso o cliente já exista.
            comando = f'INSERT INTO table_cliente (nome_cliente,endereco_cliente,email_cliente,cpf_cliente,telefone_cliente) VALUES\
            ("{Cliente.nome}", "{Cliente.endereco}", "{Cliente.email}", "{Cliente.cpf}", {Cliente.telefone})'
            #Executa o comando na base de dados 
            file_sql.cursor.execute(comando)
            # Edita o banco de dados
            file_sql.conexao.commit() 

    def realizarVenda(self):
        pass
    def cancelarVenda(self):
        pass
    def incluirMaterial(self):
        #Inserindo material na base de dados
        #Preciso fazer uma condicional aqui para caso o material já exista.
        comando = f'INSERT INTO table_material (nome_material,quantidade_material,preco_material,especificacao_material,dataFabricacao_material,fornecedor_material) VALUES\
        ("{Material.nome}", {Material.quantidade}, {Material.preco}, "{Material.especificacao}", {Material.datafabricacao}, "{Material.fornecedor}")'
        #Executa o comando na base de dados 
        file_sql.cursor.execute(comando)
        # Edita o banco de dados
        file_sql.conexao.commit() 
    def consultarVendas(self):
        pass