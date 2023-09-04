import streamlit as st
import controllers.funcionario_controllers as funcionario_controller
import models.funcionario as funcionario

# Criando o formulário para o funcionário
def criar():

    id_alteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    funcionario_recuperado = None

    if id_alteracao.get("id") != None:
        id_alteracao = id_alteracao.get("id")[0]
        funcionario_recuperado = funcionario_controller.selecionar_id(id_alteracao)
        #Talvez tenha uma erro aqui quando por conta do id
        st.experimental_set_query_params(id=[funcionario_recuperado.id])
        st.title("Alterar Funcionário")
    else:
        st.title("Incluir")

    st.subheader("Incluir Funcionário")
    with st.form(key = "Armazenar_funcionario"):
        if funcionario_recuperado == None:
            input_nome = st.text_input(label="Insira seu nome:")
            input_idade = st.number_input(label="Insira sua idade:",format="%d",step=1)
            input_cpf = st.text_input(label="Insira seu CPF:")
            input_telefone = st.text_input(label="Insira seu Telefone:")
            input_endereco = st.text_input(label="Insira seu Endereço:")
        else:
            input_nome = st.text_input(label="Insira seu nome:",value=funcionario_recuperado.nome)
            input_idade = st.number_input(label="Insira sua idade:",format="%d",step=1,value=funcionario_recuperado.idade)
            input_cpf = st.text_input(label="Insira seu CPF:",value=funcionario_recuperado.cpf)
            input_telefone = st.text_input(label="Insira seu Telefone:",value=funcionario_recuperado.telefone)
            #Eu vou conferir no vídeo e colocar as 3 opcoes disponíveis
            input_cargo = st.text_input(label="Selecione seu cargo: ",options=["Caixa","Atendente","Gerente","Estoquistas","Entregadores"],value=funcionario_recuperado.cargo)
            input_endereco = st.text_input(label="Insira seu Endereço:",value=funcionario_recuperado.endereco)
        input_botão_enviar = st.form_submit_button("Enviar")


    if input_botão_enviar:
        if funcionario_recuperado == None:
            funcionario_controller.inserir(funcionario.Funcionario(0, input_nome,input_idade,input_cpf,input_telefone,input_cargo,input_endereco))
            st.success("Funcionário incluido com sucesso !!")
        else:
            st.experimental_set_query_params()
            funcionario_controller.alterar(funcionario.Funcionario(0, input_nome,input_idade,input_cpf,input_telefone,input_cargo,input_endereco))
            st.success("Funcionário alterado com sucesso !!")