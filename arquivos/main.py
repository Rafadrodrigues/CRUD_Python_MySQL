#Local onde vai ser executado o código do sistema
from classFuncionarios import Funcionario
from classCliente import Cliente
from classMaterial import Material
from classSistema import Sistema
from classVenda import Venda
from classLogin import Login
from time import sleep
import Banco_de_dados
import os

def inicio():
    #Recebendo o usuário e mostrando as opções
    print("Seja bem-vindo a Constrular LTDA\n" + 35 * "-" + "\nComo posso ajudar?")
    print("01 - Cadastrar Funcionário.\n02 - Cadastrar Cliente.\n03 - Registrar Venda.\n04 - Cadastrar Material.\n05 - Consultar Vendas.\n06 - Cancelar Venda. \n07 - Remover funcionário. \n08- Sair.")

#Funcao responsável por direcionar a escolha feita pelo usuário
def escolher_opcao(opcao):
    if opcao == "01":
        Sistema.incluir_funcionario(Funcionario)
    elif opcao == "02":
        Sistema.incluir_cliente(Cliente)
    elif opcao == "03":
        Sistema.incluir_venda(Venda)
    elif opcao == "04":
        Sistema.incluir_material(Material)
    elif opcao == "05":
        Sistema.consultar_vendas()
    elif opcao == "06":
        Sistema.cancelar_venda()
    elif opcao == "07":
        Sistema.desativa_funcionario()
    elif opcao == "08":
        quit()

def continuar() -> bool:
    continuar = input("Deseja continuar S/N: ")
    if continuar.capitalize == 'S':
        return True
    else:
        print("Sistema finalizado. ")
        return False
    
#Essa função retornar até que o usuario insira alguma credencial correta
def liberar_acesso():
    # Realizando login
    print('---------------LOGIN----------------')
    while True:
        liberaracao = Banco_de_dados.verificar_credenciais(Login)
        if liberaracao != True:
            continue
        else:
            break
    
def primeiro_usuario():
    #Criando o primeiro usuario para que ele tenha acesso ao sistema
    print('Olá, forneça seus dados por favor. ')
    Sistema.incluir_funcionario(Funcionario)

#Caso a opcão seja selecionada, a função vai ser chamada e realizada
if __name__=="__main__":

    #Verificando se o login está correto para prosseguir no sistema
    # for i in range(0,1):
    #     primeiro_usuario()
    #     sleep(2)
    #     os.system("cls")
        
    #Após isso faremos a verificacao
    liberar_acesso()

    #Inicializando as opções
    while True:
        #Preciso agora apenas colocar as opções de realizar login que depois vai liberar o acesso ao programa
        inicio()
        opcao = input("Digite a opção desejada: ")
        os.system("cls")
        escolher_opcao(opcao)
        continuar()


