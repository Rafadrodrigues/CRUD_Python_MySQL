import streamlit as st
import pages.Material.consultar as page_consultar_material
import pages.Material.incluir as page_incluir_material

st.subheader("Página dos Materiais")

choice = st.sidebar.selectbox("Menu: ",['Cadastar','Consultar'])

if choice == "Consultar":
   page_consultar_material.consultar()

if choice == "Cadastar":
    st.experimental_set_query_params()
    page_incluir_material.criar()