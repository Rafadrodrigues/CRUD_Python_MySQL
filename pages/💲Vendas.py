import streamlit as st
import pages.Venda.consultar as page_consultar_venda
import pages.Venda.incluir as page_incluir_venda

st.subheader("Página de Vendas")

choice = st.sidebar.selectbox("Menu: ",['Cadastar','Consultar'])

if choice == "Consultar":
   page_consultar_venda.consultar()

if choice == "Cadastar":
    st.experimental_set_query_params()
    page_incluir_venda.criar()