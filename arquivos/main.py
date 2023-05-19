#Local onde vai ser executado o código do sistema
from classFuncionarios import Funcionario
from classCliente import Cliente
from classMaterial import Material
from classSistema import Sistema
from classVenda import Venda
import os
import keyboard

print("Seja bem-vindo a Constrular LTDA\n" + 35 * "-"+"\nComo posso ajudar?")
#Mostrando as opções

print("01 - Cadastrar Funcionário.\n02 - Cadastrar Cliente.\n03 - Registrar Venda.\n04 - Cadastrar Material.\n05 - Consultar Vendas.\n06 - Cancelar Venda. \n07 - Remover funcionário. \n08- Sair.")

#Funcao responsável por direcionar a escolha feita pelo usuário
def escolherOpcao(opcao):
    if opcao == "01":
        Sistema.incluirFuncionario(Funcionario)
    elif opcao == "02":
        Sistema.incluirCliente(Cliente)
    elif opcao == "03":
        Sistema.incluirVenda(Venda)
    elif opcao == "04":
        Sistema.incluirMaterial(Material)
    elif opcao == "05":
        Sistema.consultarVendas()
    elif opcao == "06":
        Sistema.cancelarVenda()
    elif opcao == "07":
        Sistema.desativaFuncionario()
    elif opcao == "08":
        quit()

#Caso a opcão seja selecionada, a função vai ser chamada e realizada
if __name__=="__main__":
    #Inserindo as opções
    while True:
        if Sistema.efetuarLogin() == True:
            opcao = input("Digite a opção desejada: ")
            os.system("cls")
            escolherOpcao(opcao)
        else:
            print('Acesso negano')

