#Local onde vai ser executado o código do sistema
from classColaboradores import Colaboradores
from classCliente import Cliente
from classMaterial import Material
from classSistema import Sistema
from classVenda import Venda
import os

print("Seja bem-vindo a Constrular LTDA\n" + 35 * "-"+"\nComo posso ajudar?")
#Mostrando as opções
print("01 - Cadastrar Colaborador.\n02 - Cadastrar Cliente.\n03 - Registrar Venda.\n04 - Cadastrar Material.\n05 - Vizualizar Vendas.\n06 - Cancelar Venda.")

def escolherOpcao(opcao):
    if opcao == "01":
        Sistema.incluirColaborador(Colaboradores)
    elif opcao == "02":
        Sistema.incluirCliente(Cliente)
    elif opcao == "03":
        Sistema.incluirVenda(Venda)
    elif opcao == "04":
        Sistema.incluirMaterial(Material)
    elif opcao == "05":
        Sistema.visualizarVendas()
    elif opcao == "06":
        Sistema.cancelarVenda()

#Caso a opcão seja selecionada, a função vai ser chamada e realizada
if __name__=="__main__":
    #Inserindo as opções
    while True:
        opcao = input("Digite a opção desejada: ")
        os.system("cls")
        escolherOpcao(opcao)

