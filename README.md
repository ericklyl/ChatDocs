# ChatPDF - Converse com seus Documentos PDF

Um aplicativo intuitivo para extrair informações e insights de documentos PDF utilizando conversa natural com IA.

## 📋 Descrição

ChatPDF transforma a experiência de interação com documentos PDF. Carregue seus arquivos e faça perguntas em linguagem natural para obter respostas precisas baseadas no conteúdo, sem precisar ler todo o material.

## ✨ Funcionalidades

- **Upload Simples**: Carregue múltiplos documentos PDF com facilidade
- **Interface Conversacional**: Interaja com seus documentos através de um chat intuitivo
- **Respostas Contextuais**: Receba informações precisas extraídas diretamente dos seus PDFs
- **Análise de Sentimento**: Identifique o tom emocional das respostas
- **Feedback Visual**: Acompanhe o progresso de processamento dos documentos
- **Design Minimalista**: Interface limpa e fácil de usar para maior produtividade

## 🔧 Tecnologias Utilizadas

- **Python**: Linguagem base do aplicativo
- **Streamlit**: Framework para a interface de usuário
- **LangChain**: Orquestração de componentes de IA
- **OpenAI**: Modelo de linguagem para processamento
- **TextBlob**: Análise de sentimento das respostas
- **FAISS/Chroma**: Armazenamento e busca eficiente de vetores

## 💼 Casos de Uso

- **Área Acadêmica**: Análise rápida de artigos científicos e pesquisas
- **Negócios**: Extração de informações de relatórios e documentação
- **Legal**: Consulta a contratos e documentos jurídicos
- **RH**: Processamento de currículos e documentação de candidatos
- **Pesquisa**: Consolidação de informações de múltiplas fontes

## 🚀 Como Usar

### Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/chatpdf.git
   cd chatpdf
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Configure sua chave de API OpenAI:
   ```
   # No arquivo .env
   OPENAI_API_KEY=sua-chave-aqui
   ```

### Execução

1. Inicie o aplicativo:
   ```
   streamlit run app.py
   ```

2. Siga estas etapas na interface:
   - Carregue seus documentos PDF na barra lateral
   - Clique em "Iniciar Chatbot" para processar os documentos
   - Faça perguntas no campo de chat
   - Observe as respostas e as análises de sentimento correspondentes

## 📈 Destaques Técnicos

- **Processamento Inteligente**: Divide documentos em blocos semanticamente relevantes
- **Vetorização Eficiente**: Utiliza embeddings para representação vetorial do texto
- **Recuperação Aumentada**: Implementa RAG (Retrieval Augmented Generation) para respostas precisas
- **Feedback Contextual**: Análise de sentimento para entender o tom emocional das respostas
- **Feedback Visual**: Barra de progresso personalizada durante o processamento

## 📦 Requisitos

- Python 3.8+
- Bibliotecas listadas em `requirements.txt`
- Chave de API OpenAI válida
- Espaço em disco para armazenamento de vetores

Desenvolvido como projeto educacional de Inteligência Artificial e Processamento de Linguagem Natural.
