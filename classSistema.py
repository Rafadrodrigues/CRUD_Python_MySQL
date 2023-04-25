from classColaboradores import Colaboradores
#from classCliente import Cliente

class Sistema(Colaboradores,):

    def __init__(self) -> None:
        self._colaboradores = []
        self._vendas=[]
        self._clientes=[]
        self._material=[]
    
    def incluirColaborador(self,colaborador):
        colaborador = Colaboradores()
        self._colaboradores = colaborador
        
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