import streamlit as st
import controllers.material_controllers as material_controllers
import models.material as material

# Criando o formulário para o material
def criar():

    id_alteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    material_recuperado = None

    if id_alteracao.get("id") != None:
        id_alteracao = id_alteracao.get("id")[0]
        material_recuperado = material_controllers.selecionar_id(id_alteracao)
        #Talvez tenha uma erro aqui quando por conta do id
        st.experimental_set_query_params(id=[material_recuperado.id])
        st.title("Alterar material")
    else:
        st.title("Incluir")

    st.subheader("Incluir Material")
    with st.form(key = "Armazenar_material"):
        if material_recuperado == None:
            input_nome = st.text_input(label="Insira seu nome:")
            input_valor = st.number_input(label="Insira o valor:",format="%2f", step=1.0)
        else:
            input_nome = st.text_input(label="Insira seu nome:",value=material_recuperado.nome)
            input_valor = st.number_input(label="Insira o valor:",format="%2f", step=1.0,value=material_recuperado.valor)
        input_botão_enviar = st.form_submit_button("Enviar")


    if input_botão_enviar:
        if material_recuperado == None:
            material_controllers.inserir(material.Material(0, input_nome,input_valor))
            st.success("Material incluido com sucesso !!")
        else:
            st.experimental_set_query_params()
            material_controllers.alterar(material.Material(0, input_nome,input_valor))
            st.success("Material alterado com sucesso !!")