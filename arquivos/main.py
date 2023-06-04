#Local onde vai ser executado o código do sistema
from classFuncionarios import Funcionario
from classCliente import Cliente
from classMaterial import Material
from classSistema import Sistema
from classVenda import Venda
from classLogin import Login
import os

def inicio():
    #Recebendo o usuário e mostrando as opções
    print("Seja bem-vindo a Constrular LTDA\n" + 35 * "-" + "\nComo posso ajudar?")
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

def continuar() -> bool:
    continuar = input("Deseja continuar: S/N")
    if continuar.capitalize == 'S':
        return True
    else:
        print("Sistema finalizado. ")
        return False

#Caso a opcão seja selecionada, a função vai ser chamada e realizada
if __name__=="__main__":
    
    #Inserindo as opções
    Login(
        input('Insira seu usuário: '),
        input('Insira sua senha: '),
    )
    
    while True:
        #Preciso agora apenas colocar as opções de realizar login que depois vai liberar o acesso ao programa
        Sistema.efetuarLogin(Login)
        os.system("cls")
        inicio()
        opcao = input("Digite a opção desejada: ")
        os.system("cls")
        escolherOpcao(opcao)
        continuar()


