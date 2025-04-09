import streamlit as st
import time
from pathlib import Path
from backend import criar_conversa, pasta_arquivos


st.set_page_config(page_title="ChatPDF")

def app_chat():
    
    st.title("Chat com PDFs - Converse com seu Docs")
    
    #olha se o chat foi iniciado
    if "chain" not in st.session_state:
        st.error("Você precisa carregar PDFs e inicializar o chatbot primeiro!")
        st.stop()
    
    #pega a chain das msgs anteriores
    chain = st.session_state["chain"]
    memory = chain.memory
    mensagens = memory.load_memory_variables({})["chat_history"]

    container = st.container()
    for mensagem in mensagens:
        chat = container.chat_message(mensagem.type)
        chat.write(mensagem.content)
    
    
    nova_mensagem = st.chat_input("Digite sua pergunta aqui")
    if nova_mensagem:
        
        chat = container.chat_message("human")
        chat.write(nova_mensagem)
        chat = container.chat_message("ai")
        chat.write("Pensando...")
        resultado = chain.invoke({"question": nova_mensagem})
        chat.empty()
        chat.write(resultado["answer"])
        
        st.rerun()

def salvar_arquivos(arquivos, pasta):
    """Função simples para salvar os arquivos enviados"""
    # cria pasta se não existir
    pasta.mkdir(exist_ok=True)

    for arquivo in pasta.glob("*.pdf"):
        arquivo.unlink()
    
    #salva arquivos
    for arquivo in arquivos:
        caminho = pasta / arquivo.name
        caminho.write_bytes(arquivo.read())

def main():

    with st.sidebar:
        st.header("Carregue os PDFs")
        
        #upload de PDFs
        arquivos_pdf = st.file_uploader(
            "Carregue seus arquivos PDF", 
            type="pdf", 
            accept_multiple_files=True
        )
        
        #salvar arquivos
        if arquivos_pdf:
            salvar_arquivos(arquivos_pdf, pasta_arquivos)
            st.success(f"{len(arquivos_pdf)} arquivos foram enviados!")
        
        arquivos_disponiveis = list(pasta_arquivos.glob("*.pdf"))
        if arquivos_disponiveis:
            st.write("Arquivos carregados:")
            for arquivo in arquivos_disponiveis:
                st.write(f"- {arquivo.name}")
        
        texto_botao = "Iniciar Chatbot" if "chain" not in st.session_state else "Reiniciar Chatbot"
        if st.button(texto_botao, use_container_width=True):
            if len(list(pasta_arquivos.glob("*.pdf"))) == 0:
                st.error("Você precisa adicionar pelo menos um arquivo PDF!")
            else:
                st.info("Inicializando o chatbot, por favor aguarde...")
                criar_conversa()
                st.success("Chatbot pronto!")
                st.rerun()
    
    # Área principal - chat
    app_chat()

if __name__ == "__main__":
    main()