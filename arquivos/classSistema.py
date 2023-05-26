from classFuncionarios import Funcionario
from classCliente import Cliente
from classVenda import Venda
from classMaterial import Material
import crudSistema

#Classe referente analise realizada no banco de dados 
class Sistema:
    def __init__(self) -> None:
        pass

    #Funcoes responsável por realizar atualizações na base de dados
    def incluirFuncionario(self):
        #Inserindo colaborador na base de dados
        crudSistema.funcionario(Funcionario) 

    def incluirCliente(self):
        #Inserindo cliente na base de dados
        crudSistema.cliente(Cliente)
            
    def realizarVenda(self):
        #Inserindo venda na base de dados
        crudSistema.venda(Venda)
        Venda.gerarNota(Material,Cliente)

    def cancelarVenda(self):
        #Cancelando venda na base de dados
        crudSistema.cancelaVenda(Venda)

    def consultarVendas():
        #Consultando material na base de dados
        crudSistema.vizualizarVenda()

    def incluirMaterial(self):
        #Inserindo material na base de dados
        crudSistema.material(Material)
    
    def desativaFuncionario():
        #Removendo funcionário da base de dados
        crudSistema.removerFuncionario()

    def efetuarLogin(Funcionario):
        #Efetuando login no sistema, mas antes verificando as credenciais
        crudSistema.verificarCredenciais(Funcionario)

        
    