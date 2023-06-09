#Local onde vai ser executado o código do sistema
from classFuncionarios import Funcionario
from classCliente import Cliente
from classMaterial import Material
from classSistema import Sistema
from classVenda import Venda
from classLogin import Login
from time import sleep
import os

def inicio():
    #Recebendo o usuário e mostrando as opções
    print("Seja bem-vindo a Constrular LTDA\n" + 35 * "-" + "\nComo posso ajudar?")
    print("[1] - Cadastrar Funcionário.\n[2] - Cadastrar Cliente.\n[3] - Registrar Venda.\n[4] - Cadastrar Material.\n[5] - Consultar Vendas.\n[6] - Cancelar Venda. \n[7] - Remover funcionário. \n[8]- Sair.")

#Funcao responsável por direcionar a escolha feita pelo usuário
def escolher_opcao(opcao):
    if opcao == "1":
        Sistema.incluir_funcionario(Funcionario)
    elif opcao == "2":
        Sistema.incluir_cliente(Cliente)
    elif opcao == "3":
        Sistema.realizar_venda(Venda)
    elif opcao == "4":
        Sistema.incluir_material(Material)
    elif opcao == "5":
        Sistema.consultar_vendas()
    elif opcao == "6":
        Sistema.cancelar_venda()
    elif opcao == "7":
        Sistema.desativa_funcionario()
    elif opcao == "8":
        quit()

def continuar() -> bool:
    continuar = input("Deseja continuar S/N: ")
    if continuar.capitalize == 'S':
        return True
    else:
        print("Sistema finalizado. ")
        return False
    
# #Essa função retornar até que o usuario insira alguma credencial correta
# def liberar_acesso():
#     # Realizando login
#     print('---------------LOGIN----------------')
#     while True:
#         liberaracao = Banco_de_dados.verificar_credenciais(Login)
#         if liberaracao != True:
#             continue
#         else:
#             break
    
# def primeiro_usuario():
#     #Criando o primeiro usuario para que ele tenha acesso ao sistema
#     print('Olá, forneça seus dados por favor. ')
#     Sistema.incluir_funcionario(Funcionario)

#Caso a opcão seja selecionada, a função vai ser chamada e realizada
if __name__=="__main__":
    
    #Inicializando as opções
    while True:
        #Preciso agora apenas colocar as opções de realizar login que depois vai liberar o acesso ao programaa
        inicio()
        opcao = input("Digite a opção desejada: ")
        os.system("cls")
        escolher_opcao(opcao)
        continuar()

'''                                     IMPORTANTE
Eu criei esse projeto para tentar testar meus conhecimentos em orientacao a objetos e integraçao com 
banco de dados, porém, futuramente, vou estar realizando uma manutenção no código e pretendo integralo
com alguma interface grafica e deixa-lo com "mais cara " de Python. Esse é um planejamento que pretendo 
para o mês de agosto, mes que vou estar de ferias da faculdade e consequentemente vou ter mais tempo
para dar atençao"'''


