from classMaterial import Material
from classCliente import Cliente
from datetime import datetime
import pytz

#Classe responsável pelo vendas realizada 
class Venda:

    #Método responsável por fornecer data e hora
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%y %H:%M:%S')

    def __init__(self,valorTotal) -> None:
        self._idVenda = ""
        self._data = Venda._data_hora()
        self._valorTotal = valorTotal

    #Fornecendo caracteristica das vendas por meio getter e setter
    @property
    def idVenda(self):
        return self._idVenda
    @idVenda.setter
    def idVenda(self,idVenda):
        self._idVenda = idVenda
        
    @property
    def valorTotal(self):
        return self._valorTotal
    @valorTotal.setter
    def valorTotal(self,valorTotal):
        self._valorTotal = valorTotal
    
    #Funcao responsável por gerar nota
    def gerarNota(self,Material,Cliente):
        
        escolha = input("Deseja nome e CPF na nota? S/N: ")

        if escolha.capitalize() == "S":
            print(f"Vendidos {Material.quantidade} quantidades de {Material.nome} por {Material.preco}.\
            \nNome cliente:{Cliente.nome} CPF:{Cliente.cpf}\
            \nData:{self._data}.\nValor total da venda:{self._valorTotal}")
        else:
            print(f"Vendidos {Material.quantidade} quantidades do {Material.nome} por {Material.preco}.\
            \nData:{self._data}.\nValor total da venda:{self._valorTotal}")

print("Loja Construção LTDA\n" + 20 * "-")
novo_cliente = Cliente("Rafael"," ","rafa@hotmail.com",121,33)
nome = Material("Porca",20,1200," ","20/10/2021","Ponto mágico")
data = Venda(300)

print(data.gerarNota(nome,novo_cliente))