class Cliente:

    def __init__(self,id:int,nome:str,idade:int,cpf:str,telefone:str,endereco:str) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco

# # Criando o formulário para o Material
# st.subheader("Inserindo informações dos material.")
# with st.form(key = "Armazenar_material"):
#     input_nome = st.text_input(label="Insira seu nome:")
#     input_valor = st.number_input(label="Qual o valor:",step=0.1)
#     input_data= st.date_input(label="Selecione uma data:")

# # Criando o formulário para o Venda
# st.subheader("Inserindo informações das vendas.")
# with st.form(key = "Armazenar_vendas"):
#     input_nome = st.text_input(label="Insira seu nome:")
#     input_quantidade = st.number_input(label="Quanidade:",format="%d",step=1)
#     input_valor = st.number_input(label="Qual o valor:",step=0.1)
#     input_botão_enviar = st.form_submit_button("Enviar")
