import streamlit as st
import controllers.cliente_controllers as cliente_controller
import models.cliente as cliente

# Criando o formulário para o cliente
def criar():

    id_alteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    cliente_recuperado = None

    if id_alteracao.get("id") != None:
        id_alteracao = id_alteracao.get("id")[0]
        cliente_recuperado = cliente_controller.selecionar_id(id_alteracao)
        #Talvez tenha uma erro aqui quando por conta do id
        st.experimental_set_query_params(id=[cliente_recuperado.id])
        st.title("Alterar cliente")
    else:
        st.title("Incluir")

    st.subheader("Incluir Cliente")
    with st.form(key = "Armazenar_cliente"):
        if cliente_recuperado == None:
            input_nome = st.text_input(label="Insira seu nome:")
            input_idade = st.number_input(label="Insira sua idade:",format="%d",step=1)
            input_cpf = st.text_input(label="Insira seu CPF:")
            input_telefone = st.text_input(label="Insira seu Telefone:")
            input_endereco = st.text_input(label="Insira seu Endereço:")
        else:
            input_nome = st.text_input(label="Insira seu nome:",value=cliente_recuperado.nome)
            input_idade = st.number_input(label="Insira sua idade:",format="%d",step=1,value=cliente_recuperado.idade)
            input_cpf = st.text_input(label="Insira seu CPF:",value=cliente_recuperado.cpf)
            input_telefone = st.text_input(label="Insira seu Telefone:",value=cliente_recuperado.telefone)
            input_endereco = st.text_input(label="Insira seu Endereço:",value=cliente_recuperado.endereco)
        input_botão_enviar = st.form_submit_button("Enviar")


    if input_botão_enviar:
        if cliente_recuperado == None:
            cliente_controller.inserir(cliente.Cliente(0, input_nome,input_idade,input_cpf,input_telefone,input_endereco))
            st.success("Cliente incluido com sucesso !!")
        else:
            st.experimental_set_query_params()
            cliente_controller.alterar(cliente.Cliente(0, input_nome,input_idade,input_cpf,input_telefone,input_endereco))
            st.success("Cliente alterado com sucesso !!")