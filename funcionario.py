import streamlit as st

st.set_page_config(page_title="Funcionários")

st.title("Inserindo funcionários")

# Criando o formulário para o funcionário
with st.form(key = "Armazenar_funcionario"):
    input_nome = st.text_input(label="Insira seu nome:")
    input_idade = st.number_input(label="Insira sua idade:",format="%d",step=1)
    input_cpf = st.text_input(label="Insira seu CPF:")
    input_telefone = st.text_input(label="Insira seu Telefone:")
    input_cargo = st.selectbox(label="Selecione usa profissao",options=["Atendente,Gerente,Administrador"])
    input_endereco = st.text_input(label="Insira seu Endereço:")
    input_botão_enviar = st.form_submit_button("Enviar")

if input_botão_enviar:
    st.write(f'Nome: {input_nome}')
    st.write(f'Idade: {input_idade}')
    st.write(f'Cpf: {input_cpf}')
    st.write(f'Telefone: {input_telefone}')
    st.write(f'Cargo: {input_cargo}')
    st.write(f'Endereço: {input_endereco}')