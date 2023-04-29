from classMaterial import Material
from classCliente import Cliente
from datetime import datetime, timedelta
import pytz

#Classe responsável pelo vendas realizada 
class Venda:

    #Método responsável por fornecer data e hora
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%y %H:%M:%S')

    def __init__(self) -> None:
        self._idVenda = ""
        self._data = Venda._data_hora()
        self._valorTotal = None

    #Fornecendo caracteristica das vendas por meio getter e setter
    @property
    def _idVenda(self):
        return self._idVenda
    @_idVenda.setter
    def _idVenda(self,idVenda):
        self._idVenda = idVenda
        
    @property
    def _valorTotal(self):
        return self._valorTotal
    @_valorTotal.setter
    def _valorTotal(self,valorTotal):
        self._valorTotal = valorTotal
    
    #Funcao responsável por gerar nota
    def gerarNota(self):
        material_vendido = Material()
        info_cliente = Cliente()
        
        escolha = input("Deseja nome e CPF na nota? S/N")

        if escolha.capitalize() == "S":
            print(f"Vendidos {material_vendido.quantidade()} quantidades do {material_vendido.nome()}\
            por {material_vendido.preco()}.\nNome cliente:{info_cliente.nome()} CPF:{info_cliente.cpf()}\n\
            Data:{self._data}.\nValor total da venda:{self._valorTotal}")
        else:
            print(f"Vendidos {material_vendido.quantidade()} quantidades do {material_vendido.nome()}\
            por {material_vendido.preco()}.\nData:{self._data}.\nValor total da venda:{self._valorTotal}")

        
