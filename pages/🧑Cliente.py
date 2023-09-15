import streamlit as st
import pages.Cliente.incluir as page_incluir_cliente
import pages.Cliente.consultar as page_consultar_cliente

st.subheader("Página do Cliente")

choice = st.sidebar.selectbox("Menu: ",['Cadastar','Consultar'])
if choice == "Cadastar":
    st.subheader("Cadastar")

#Opções correspondente ao cliente
if choice == "Consultar":
   page_consultar_cliente.consultar()

if choice == "Cadastar":
    st.experimental_set_query_params()
    page_incluir_cliente.criar()