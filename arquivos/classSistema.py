from classColaboradores import Colaboradores
from classCliente import Cliente
import crudSistema

#Classe referente analise realizada no banco de dados 
class Sistema:
    def __init__(self,login,senha) -> None:
        self.colaboradores = Colaboradores(login,senha)
        self.clientes = Cliente(login,senha)

    #Funcoes responsável por realizar atualizações na base de dados
    def incluirColaborador(self):
        #Inserindo colaborador na base de dados
        crudSistema.colaborador() 

    def incluirCliente(self):
        #Inserindo cliente na base de dados
        crudSistema.cliente()
            
    def realizarVenda(self,):
        #Inserindo venda na base de dados
        crudSistema.venda()

    def cancelarVenda(self):
        #Cancelando venda na base de dados
        crudSistema.cancelaVenda()

    def consultarVendas(self):
        #Consultando material na base de dados
        crudSistema.vizualizarVenda()

    def incluirMaterial(self,Material):
        #Inserindo material na base de dados
        crudSistema.material()

    