import streamlit as st
import time
from pathlib import Path
from backend import criar_conversa, pasta_arquivos 


st.set_page_config(page_title="ChatDocuments")

def app_chat():

    st.title("Chat com Documentos - Converse com PDFs, DOCX, TXT e ODT")

    if "chain" not in st.session_state:
        st.error("Você precisa carregar documentos (PDF, DOCX, TXT ou ODT) e inicializar o chatbot primeiro!")
        st.stop() 

    chain = st.session_state["chain"]
    memory = chain.memory
    mensagens = memory.load_memory_variables({})["chat_history"]

    container = st.container()
    for mensagem in mensagens:
        chat = container.chat_message(mensagem.type) # 'human' ou 'ai'
        chat.write(mensagem.content)


    nova_mensagem = st.chat_input("Digite sua pergunta aqui")
    if nova_mensagem:
        
        chat = container.chat_message("human")
        chat.markdown(nova_mensagem)

        chat = container.chat_message("ai")
        with st.spinner("🧠 Gerando resposta..."): 
            result = chain.invoke({"question": nova_mensagem})
            chat.markdown(result["answer"]) # Exibe a resposta do chatbot

            

        st.rerun() 

def salvar_arquivos(arquivos, pasta):
    """Função para salvar os arquivos enviados pelo usuário na pasta 'arquivos'."""
    # Cria a pasta se não existir
    pasta.mkdir(exist_ok=True)

    
    for arquivo in pasta.glob("*.pdf"):
        arquivo.unlink()
    for arquivo in pasta.glob("*.docx"):
        arquivo.unlink()
    for arquivo in pasta.glob("*.txt"):
        arquivo.unlink()
    for arquivo in pasta.glob("*.odt"):
        arquivo.unlink()

    for arquivo in arquivos:
        caminho = pasta / arquivo.name
        caminho.write_bytes(arquivo.read())

def mostrar_progresso_processamento():
    """Mostra uma barra de progresso personalizada durante o processamento inicial do chatbot."""
    progress_bar = st.progress(0)
    status_text = st.empty()

    status_text.text("🔍 Carregando documentos...")
    progress_bar.progress(25)
    time.sleep(0.7)

    status_text.text("📄 Processando texto...")
    progress_bar.progress(50)
    time.sleep(0.7)

    status_text.text("🧠 Criando embeddings...")
    progress_bar.progress(75)
    time.sleep(0.7)

    status_text.text("✅ Finalizando...")
    progress_bar.progress(100)
    status_text.text("✅ Processamento concluído!")
    time.sleep(0.5)


def main():
    """Função principal que organiza a interface do Streamlit."""
    with st.sidebar: 
        st.header("Carregue os Documentos")

        arquivos_documentos = st.file_uploader(
            "Carregue seus arquivos (PDF, DOCX, TXT, ODT)",
            type=["pdf", "docx", "txt", "odt"],
            accept_multiple_files=True
        )

        if arquivos_documentos:
            salvar_arquivos(arquivos_documentos, pasta_arquivos)
            st.success(f"{len(arquivos_documentos)} arquivos foram enviados!")

        arquivos_disponiveis = []
        arquivos_disponiveis.extend(list(pasta_arquivos.glob("*.pdf")))
        arquivos_disponiveis.extend(list(pasta_arquivos.glob("*.docx")))
        arquivos_disponiveis.extend(list(pasta_arquivos.glob("*.txt")))
        arquivos_disponiveis.extend(list(pasta_arquivos.glob("*.odt")))

        if arquivos_disponiveis:
            st.write("Arquivos carregados:")
            for arquivo in arquivos_disponiveis:
                if arquivo.suffix.lower() == '.pdf':
                    icone = "📄"
                elif arquivo.suffix.lower() == '.docx':
                    icone = "📝"
                elif arquivo.suffix.lower() == '.txt':
                    icone = "📃"
                elif arquivo.suffix.lower() == '.odt':
                    icone = "📄"
                else:
                    icone = "📋" # Ícone padrão
                st.write(f"{icone} {arquivo.name}")

        texto_botao = "Iniciar Chatbot" if "chain" not in st.session_state else "Reiniciar Chatbot"

        if st.button(texto_botao, use_container_width=True, type="primary"):
            total_arquivos = (
                len(list(pasta_arquivos.glob("*.pdf"))) +
                len(list(pasta_arquivos.glob("*.docx"))) +
                len(list(pasta_arquivos.glob("*.txt"))) +
                len(list(pasta_arquivos.glob("*.odt")))
            )
            if total_arquivos == 0:
                st.error("Adicione arquivos (PDF, DOCX, TXT ou ODT) para inicializar o chatbot")
            else:
                with st.spinner("⏳ Inicializando..."):
                    mostrar_progresso_processamento() 
                    criar_conversa() 
                st.success("✅ Chatbot pronto!")
                st.rerun() 

    app_chat() 

if __name__ == "__main__":
    main() 
