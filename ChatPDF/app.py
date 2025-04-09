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
        chat.markdown(nova_mensagem)
        
        chat = container.chat_message("ai")
        with st.spinner("🧠 Gerando resposta..."):
            result = chain.invoke({"question": nova_mensagem})
            chat.markdown(result["answer"])
            
            sentimento, emoji, cor = analisar_sentimento(result["answer"])
            chat.markdown(f"""
            <div style="margin-top: 10px; padding: 5px 10px; border-radius: 5px; background-color: {cor}25; display: inline-block;">
                <span style="color: {cor}; font-weight: bold;">Sentimento: {sentimento} {emoji}</span>
            </div>
            """, unsafe_allow_html=True)
        
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

def mostrar_progresso_processamento():
    """Mostra uma barra de progresso personalizada durante o processamento."""
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

def analisar_sentimento(texto):
    """Analisa o sentimento do texto e retorna uma classificação simples."""
    from textblob import TextBlob
    
    blob = TextBlob(texto)
    sentimento = blob.sentiment.polarity
    
    if sentimento > 0.1:
        return "Positivo", "😃", "#28a745"  
    elif sentimento < -0.1:
        return "Negativo", "😔", "#dc3545"  
    else:
        return "Neutro", "😐", "#6c757d"  

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
        
        if st.button(texto_botao, use_container_width=True, type="primary"):
            if len(list(pasta_arquivos.glob("*.pdf"))) == 0:
                st.error("Adicione arquivos PDF para inicializar o chatbot")
            else:
                with st.spinner("⏳ Inicializando..."):
                    mostrar_progresso_processamento()  
                    criar_conversa()
                st.success("✅ Chatbot pronto!")
                st.rerun()
    
    app_chat()

if __name__ == "__main__":
    main()