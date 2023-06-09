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

    def __init__(self,valor_total:float,data:str) -> None:
        self._data = data
        self._valor_total = valor_total

    #Fornecendo caracteristica das vendas por meio getter e setter
    @property
    def data(self)-> float:
        return self._data
    @data.setter
    def data(self,data:str):
        self._data = data
        
    @property
    def valor_total(self)-> float:
        return self._valor_total
    @valor_total.setter
    def valor_total(self,valor_total:float):
        self._valor_total = valor_total
    
    #Funcao responsável por gerar nota
    def gerar_nota(self,Material,Cliente) -> str:
        
        escolha = input("Deseja nome e CPF na nota? S/N: ")

        if escolha.capitalize() == "S":
            print(f"Vendidos {Material.quantidade} quantidades de {Material.nome} por {Material.preco}.\
            \nNome cliente:{Cliente.nome} CPF:{Cliente.cpf}\
            \nData:{self.data}.\nValor total da venda:{self.valor_total}")
        else:
            print(f"Vendidos {Material.quantidade} quantidades do {Material.nome} por {Material.preco}.\
            \nData:{self.data}.\nValor total da venda:{self.valor_total}")
    
    #Essa é uma funcionalidade que quem faz é o funcionário
    def balanco_mensal(self):
        pass
