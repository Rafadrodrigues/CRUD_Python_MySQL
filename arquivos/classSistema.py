from classFuncionarios import Funcionario
from classCliente import Cliente
from classVenda import Venda
from classMaterial import Material
import Banco_de_dados

#Classe referente analise realizada no banco de dados 
#Eu posso fazer uma coisinha diferente, eu posso criar alguns métodos que são incluir, editar e remover, o que mudaria seria o tipo

class Sistema:

    def __init__(self) -> None:
        pass

    #Funcoes responsável por realizar atualizações na base de dados
    def incluir_funcionario(self):
        #Inserindo colaborador na base de dados
        Banco_de_dados.funcionario(Funcionario) 

    def incluir_cliente(self):
        #Inserindo cliente na base de dados
        Banco_de_dados.cliente(Cliente)
    
    def realizar_venda(self):
        #Inserindo venda na base de dados
        Banco_de_dados.venda(Venda)
        Venda.gerar_nota(Material,Cliente)

    def cancelar_venda(self):
        #Cancelando venda na base de dados
        Banco_de_dados.cancela_venda(Venda)

    def consultar_vendas():
        #Consultando material na base de dados
        Banco_de_dados.vizualizar_venda()

    def incluir_material(self):
        #Inserindo material na base de dados
        Banco_de_dados.material(Material)

    def desativa_funcionario():
        #Removendo funcionário da base de dados
        Banco_de_dados.remover_funcionario()
        
    def efetuar_login(Login):
        #Efetuando login no sistema, mas antes verificando as credenciais
        Banco_de_dados.verificar_credenciais(Login)

        
    