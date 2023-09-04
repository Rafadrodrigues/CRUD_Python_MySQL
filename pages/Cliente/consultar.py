import streamlit as st
import controllers.cliente_controllers as cliente_controller
import pages.Cliente.incluir as page_create_cliente

def consultar(): 
    param_id = st.experimental_get_query_params()
    if param_id == {}:
        st.title("Consultar")

        st.subheader("Consultar Cliente")
        colunas = st.columns((2,2,2,2,2,2,2,2))

        campos = ['N°','Nome','Idade','CPF','Endereço','Telefone','Excluir', 'Alterar'] 

        for col, campo_nome in zip(colunas,campos):
            col.write(campo_nome)

        for x,item in enumerate(cliente_controller.selecionar_todos_clientes()):

            col1,col2,col3,col4,col5,col6,col7,col8 = st.columns((2,2,2,2,2,2,2,2))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.idade)
            col4.write(item.cpf)
            col5.write(item.telefone)
            col6.write(item.endereco)

            button_space_excluir = col7.empty()
            on_click_excluir = button_space_excluir.button('Excluir','btnExcluir' + str(item.id))
            button_space_alterar = col8.empty()
            on_click_alterar = button_space_alterar.button('Alterar','btnAltera' + str(item.id))

            #Realiza a função de deletar da base de dados
            if on_click_excluir:
                cliente_controller.excluir(item.id)
                button_space_excluir.button('Excluído','btnExcluir2' + str(item.id))

            #Realiza a função de alterar da base de dados
            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id]
                )
                st.experimental_rerun()
                # page_create_cliente.criar()
                # cliente_controller.excluir(item.id)
                # button_space_alterar.button('Alterado','btnAltera2' + str(item.id))

    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        page_create_cliente.criar()