import streamlit as st
import controllers.vendas_controllers as vendas_controllers
import models.vendas as venda

# Criando o formulário para o venda
def criar():

    id_alteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    venda_recuperado = None

    if id_alteracao.get("id") != None:
        id_alteracao = id_alteracao.get("id")[0]
        venda_recuperado = vendas_controllers.selecionar_id(id_alteracao)
        #Talvez tenha uma erro aqui quando por conta do id
        st.experimental_set_query_params(id=[venda_recuperado.id])
        st.title("Alterar venda")
    else:
        st.title("Incluir")

    st.subheader("Incluir Venda")
    with st.form(key = "Armazenar_venda"):
        if venda_recuperado == None:
            input_nome = st.text_input(label="Insira seu nome:")
            input_quantidade = st.number_input(label="Insira a quantidade:",format="%d",step=1)
            input_valor = st.number_input(label="Insira o valor:",format="%2f", step=1.0)
        else:
            input_nome = st.text_input(label="Insira seu nome:",value=venda_recuperado.nome)
            input_quantidade = st.number_input(label="Insira a quantidade:",format="%d",step=1,value=venda_recuperado.quantidade)
            input_valor = st.number_input(label="Insira o valor:",format="%2f", step=1.0,value=venda_recuperado.valor)
        input_botão_enviar = st.form_submit_button("Enviar")


    if input_botão_enviar:
        if venda_recuperado == None:
            vendas_controllers.inserir(venda.Venda(0, input_nome,input_quantidade,input_valor))
            st.success("Venda incluida com sucesso !!")
        else:
            st.experimental_set_query_params()
            vendas_controllers.alterar(venda.Venda(0, input_nome,input_quantidade,input_valor))
            st.success("Venda alterada com sucesso !!")