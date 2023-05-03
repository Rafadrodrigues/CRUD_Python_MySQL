from classColaboradores import Colaboradores
from classCliente import Cliente
from classVenda import Venda
from classMaterial import Material
import crudSistema

#Classe referente analise realizada no banco de dados 
class Sistema:
    def __init__(self,login,senha) -> None:
        self.clientes = Cliente(login,senha)

    #Funcoes responsável por realizar atualizações na base de dados
    def incluirColaborador(self):
        #Inserindo colaborador na base de dados
        crudSistema.colaborador(Colaboradores) 

    def incluirCliente(self):
        #Inserindo cliente na base de dados
        crudSistema.cliente(Cliente)
            
    def realizarVenda(self):
        #Inserindo venda na base de dados
        crudSistema.venda(Venda)

    def cancelarVenda(self):
        #Cancelando venda na base de dados
        crudSistema.cancelaVenda(Venda)

    def consultarVendas(self):
        #Consultando material na base de dados
        crudSistema.vizualizarVenda()

    def incluirMaterial(self):
        #Inserindo material na base de dados
        crudSistema.material(Material)

    