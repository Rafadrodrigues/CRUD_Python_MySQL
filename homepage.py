import streamlit as st
import pages.Cliente.incluir as page_incluir_cliente
import pages.Cliente.consultar as page_consultar_cliente
import pages.Funcionario.consultar as page_consultar_funcionario
import pages.Funcionario.incluir as page_incluir_funcionario
import pages.Material.consultar as page_consultar_material
import pages.Material.incluir as page_incluir_material
import pages.Venda.consultar as page_consultar_venda
import pages.Venda.incluir as page_incluir_venda
st.set_page_config(
    page_title = "Material Construção",
    page_icon="👨‍💻",
)

st.sidebar.title("Menu de opções")

#Opções disponíveis na página principal
page_cliente = st.sidebar.selectbox("Cliente",['Incluir',"Consultar"])
page_funcionario = st.sidebar.selectbox("Funcionário",['Incluir',"Consultar"])
page_material = st.sidebar.selectbox("Material",['Incluir',"Consultar"])
page_venda = st.sidebar.selectbox("Vendas",['Incluir',"Consultar"])

#Opções correspondente ao cliente
if page_cliente == "Consultar":
   page_consultar_cliente.consultar()

if page_cliente == "Incluir":
    st.experimental_set_query_params()
    page_incluir_cliente.criar()

#Opções correspondente ao Funcionario
if page_funcionario == "Consultar":
   page_consultar_funcionario.consultar()

if page_funcionario == "Incluir":
    st.experimental_set_query_params()
    page_incluir_funcionario.criar()

#Opções correspondente ao Material
if page_material == "Consultar":
   page_consultar_material.consultar()

if page_material == "Incluir":
    st.experimental_set_query_params()
    page_incluir_material.criar()

#Opções correspondente a Venda
if page_venda == "Consultar":
   page_consultar_venda.consultar()

if page_venda == "Incluir":
    st.experimental_set_query_params()
    page_incluir_venda.criar()

