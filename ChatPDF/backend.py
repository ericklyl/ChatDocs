from pathlib import Path
import os
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_openai.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import streamlit as st
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())


pasta_arquivos = Path(__file__).parent / "arquivos"
pasta_arquivos.mkdir(exist_ok=True)


nome_modelo = "gpt-3.5-turbo-0125"

def importar_documentos():
    """Função para carregar os documentos PDF"""
    documentos = []
    for arquivo in pasta_arquivos.glob("*.pdf"):
        try:
            loader = PyPDFLoader(str(arquivo))
            docs_arquivo = loader.load()
            documentos.extend(docs_arquivo)
        except Exception as e:
            st.error(f"Erro ao carregar {arquivo.name}: {e}")
    return documentos

def dividir_documentos(documentos):
    """Função para dividir documentos em pedaços menores"""
    divisor = RecursiveCharacterTextSplitter(
        chunk_size=1000,  #tamanho de cada pedaço
        chunk_overlap=50,  #sobreposição entre pedaços
        separators=["\n\n", "\n", ".", " ", ""]
    )
    
    documentos_divididos = divisor.split_documents(documentos)
    for i, doc in enumerate(documentos_divididos):
        if "source" in doc.metadata:
            doc.metadata["source"] = Path(doc.metadata["source"]).name
        doc.metadata["id"] = i
    
    return documentos_divididos

def criar_vetores(documentos):
    """Função para criar vetores de embeddings"""
    modelo_embeddings = OpenAIEmbeddings()
    vetores = FAISS.from_documents(
        documents=documentos,
        embedding=modelo_embeddings
    )
    
    return vetores

def criar_conversa():
    """Função principal para criar a conversa"""
    st.sidebar.text("Carregando documentos...")
    
    documentos = importar_documentos()
    if not documentos:
        st.error("Nenhum documento encontrado ou carregado!")
        return None
    
    st.sidebar.text("Processando textos...")
    documentos_divididos = dividir_documentos(documentos)
    
    st.sidebar.text("Criando embeddings...")
    vetores = criar_vetores(documentos_divididos)
    
    st.sidebar.text("Configurando modelo...")
    chat = ChatOpenAI(
        model=nome_modelo,
        temperature=0.7  #nivel de criatividade e precisão do modelo
    )
    
    memoria = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )
    
    recuperador = vetores.as_retriever(
        search_kwargs={"k": 3}  #busca 3 documentos mais relevantes
    )
    
    chain_conversa = ConversationalRetrievalChain.from_llm(
        llm=chat,
        memory=memoria,
        retriever=recuperador,
        return_source_documents=True
    )
    st.session_state["chain"] = chain_conversa
    return chain_conversa