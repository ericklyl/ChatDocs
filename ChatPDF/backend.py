from pathlib import Path
import os
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader, TextLoader, UnstructuredODTLoader
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
    """Função para carregar documentos PDF, DOCX, TXT e ODT"""
    documentos = []
    print(f"DEBUG: Buscando arquivos na pasta: {pasta_arquivos}") 
    arquivos_encontrados_qualquer_tipo = False 

    # Buscar arquivos PDF
    for arquivo in pasta_arquivos.glob("*.pdf"):
        arquivos_encontrados_qualquer_tipo = True 
        print(f"DEBUG: Tentando carregar PDF: {arquivo.name}") 
        try:
            loader = PyPDFLoader(str(arquivo))
            docs_arquivo = loader.load()
            print(f"DEBUG: PDF {arquivo.name} carregado. Chunks: {len(docs_arquivo)}") 
            documentos.extend(docs_arquivo)
        except Exception as e:
            st.error(f"Erro ao carregar PDF {arquivo.name}: {e}")
            print(f"DEBUG: ERRO ao carregar PDF {arquivo.name}: {e}") 

    # Buscar arquivos DOCX
    for arquivo in pasta_arquivos.glob("*.docx"):
        arquivos_encontrados_qualquer_tipo = True 
        print(f"DEBUG: Tentando carregar DOCX: {arquivo.name}") 
        try:
            loader = Docx2txtLoader(str(arquivo))
            docs_arquivo = loader.load()
            print(f"DEBUG: DOCX {arquivo.name} carregado. Chunks: {len(docs_arquivo)}") 
            documentos.extend(docs_arquivo)
        except Exception as e:
            st.error(f"Erro ao carregar DOCX {arquivo.name}: {e}")
            print(f"DEBUG: ERRO ao carregar DOCX {arquivo.name}: {e}") 

    # Buscar arquivos ODT
    for arquivo in pasta_arquivos.glob("*.odt"):
        arquivos_encontrados_qualquer_tipo = True 
        print(f"DEBUG: Tentando carregar ODT: {arquivo.name}") 
        try:
            loader = UnstructuredODTLoader(str(arquivo))
            docs_arquivo = loader.load()
            print(f"DEBUG: ODT {arquivo.name} carregado. Chunks: {len(docs_arquivo)}") 
            documentos.extend(docs_arquivo)
        except Exception as e:
            st.error(f"Erro ao carregar ODT {arquivo.name}: {e}")
            print(f"DEBUG: ERRO ao carregar ODT {arquivo.name}: {e}") 

    # Buscar arquivos TXT
    for arquivo in pasta_arquivos.glob("*.txt"):
        arquivos_encontrados_qualquer_tipo = True 
        print(f"DEBUG: Tentando carregar TXT: {arquivo.name}") 
        try:
            loader = TextLoader(str(arquivo), encoding='utf-8')
            docs_arquivo = loader.load()
            print(f"DEBUG: TXT {arquivo.name} carregado. Chunks: {len(docs_arquivo)}") 
            documentos.extend(docs_arquivo)
        except Exception as e:
            # Tentar com encoding latin-1 se utf-8 falhar
            try:
                print(f"DEBUG: TXT {arquivo.name} - Falha UTF-8, tentando LATIN-1.") 
                loader = TextLoader(str(arquivo), encoding='latin-1')
                docs_arquivo = loader.load()
                print(f"DEBUG: TXT {arquivo.name} carregado (LATIN-1). Chunks: {len(docs_arquivo)}") 
                documentos.extend(docs_arquivo)
            except Exception as e2:
                st.error(f"Erro ao carregar TXT {arquivo.name}: {e2}")
                print(f"DEBUG: ERRO ao carregar TXT {arquivo.name}: {e2}") 

    if not arquivos_encontrados_qualquer_tipo: 
        print("DEBUG: NENHUM ARQUIVO ENCONTRADO (pdf, docx, txt, odt) na pasta 'arquivos'.") 
    elif not documentos: 
        print("DEBUG: ARQUIVOS ENCONTRADOS, mas nenhum documento foi carregado com sucesso (lista 'documentos' está vazia).") 
    else: 
        print(f"DEBUG: Total de documentos carregados (importar_documentos): {len(documentos)}") 

    return documentos

def dividir_documentos(documentos):
    """Função para dividir documentos em pedaços menores"""
    print(f"DEBUG: Total de documentos ANTES da divisão: {len(documentos)}") 
    divisor = RecursiveCharacterTextSplitter(
        chunk_size=1000,   #tamanho de cada pedaço
        chunk_overlap=50,  #sobreposição entre pedaços
        separators=["\n\n", "\n", ".", " ", ""]
    )

    documentos_divididos = divisor.split_documents(documentos)
    for i, doc in enumerate(documentos_divididos):
        if "source" in doc.metadata:
            doc.metadata["source"] = Path(doc.metadata["source"]).name
        doc.metadata["id"] = i
    print(f"DEBUG: Total de pedaços APÓS a divisão: {len(documentos_divididos)}") 

    return documentos_divididos

def criar_vetores(documentos):
    """Função para criar vetores de embeddings"""
    print("DEBUG: Criando modelo de embeddings OpenAI...") 
    modelo_embeddings = OpenAIEmbeddings()
    print("DEBUG: Criando vetor store FAISS a partir dos documentos divididos...") 
    vetores = FAISS.from_documents(
        documents=documentos,
        embedding=modelo_embeddings
    )
    print("DEBUG: Vetores criados com sucesso.") 

    return vetores

def criar_conversa():
    """Função principal para criar a conversa"""
    st.sidebar.text("Carregando documentos...")

    documentos = importar_documentos()
    if not documentos:
        st.error("Nenhum documento encontrado ou carregado!")
        print("DEBUG: criar_conversa - Nenhum documento carregado (lista 'documentos' vazia). Retornando None.") 
        return None

    st.sidebar.text("Processando textos...")
    documentos_divididos = dividir_documentos(documentos)

    if not documentos_divididos: # 
        st.error("Nenhum pedaço de documento foi gerado após a divisão. O arquivo pode estar vazio ou o splitter não conseguiu processá-lo!")
        print("DEBUG: criar_conversa - Lista 'documentos_divididos' está vazia. Retornando None.") 
        return None

    st.sidebar.text("Criando embeddings...")
    vetores = criar_vetores(documentos_divididos)
    

    st.sidebar.text("Configurando modelo...")
    chat = ChatOpenAI(
        model=nome_modelo,
        temperature=0.7   #nivel de criatividade e precisão do modelo
    )
    print("DEBUG: Modelo ChatOpenAI configurado.") 

    memoria = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )
    print("DEBUG: Memória da conversa configurada.") 

    recuperador = vetores.as_retriever(
        search_kwargs={"k": 3}   #busca 3 documentos mais relevantes
    )
    print("DEBUG: Recuperador configurado.") 

    chain_conversa = ConversationalRetrievalChain.from_llm(
        llm=chat,
        memory=memoria,
        retriever=recuperador,
        return_source_documents=True
    )
    st.session_state["chain"] = chain_conversa
    print("DEBUG: Cadeia de conversação criada e armazenada na sessão.") 
    return chain_conversa
