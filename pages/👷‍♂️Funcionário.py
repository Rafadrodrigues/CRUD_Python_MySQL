import streamlit as st
import pages.Funcionario.consultar as page_consultar_funcionario
import pages.Funcionario.incluir as page_incluir_funcionario

st.subheader("Página do Funcionário")

choice = st.sidebar.selectbox("Menu: ",['Cadastar','Consultar'])

if choice == "Consultar":
   page_consultar_funcionario.consultar()

if choice == "Cadastar":
    st.experimental_set_query_params()
    page_incluir_funcionario.criar()