from classColaboradores import Colaboradores
from classCliente import Cliente
import file_sql

#Classe referente analise realizada no banco de dados 
class Sistema(Colaboradores,Cliente):

    def __init__(self) -> None:
        self._colaboradores = []
        self._vendas=[]
        self._clientes=[]
        self._material=[]
    
    #Funcoes responsável por realizar atualizações na base de dados
    def incluirColaborador(self,colaborador):
        pass
    def incluirCliente(self):
        pass
    def realizarVenda(self):
        pass
    def cancelarVenda(self):
        pass
    def incluirMaterial(self):
        pass
    def consultarVendas(self):
        pass