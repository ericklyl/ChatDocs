# ChatPDF - Converse com seus Documentos PDF

Um aplicativo simples para conversar com seus documentos PDF usando Inteligência Artificial. Faça perguntas sobre o conteúdo dos seus arquivos e receba respostas baseadas neles.

## 📋 Descrição

ChatPDF permite que você faça upload de documentos PDF e interaja com eles através de uma interface de chat. O aplicativo utiliza processamento de linguagem natural para entender o conteúdo dos seus documentos e responder a perguntas sobre eles.

## ✨ Funcionalidades

- Upload de múltiplos arquivos PDF
- Processamento automático dos documentos
- Interface de chat intuitiva
- Respostas baseadas no conteúdo dos seus documentos
- Exibição das fontes usadas para gerar respostas

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal
- **Streamlit**: Para a interface do usuário
- **LangChain**: Para processamento de linguagem natural
- **OpenAI**: Modelo de linguagem para geração de respostas
- **PyPDFLoader**: Para carregar e processar documentos PDF
- **FAISS**: Para armazenamento e busca eficiente de vetores

## 🚀 Como Instalar e Usar

### Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)
- Chave de API da OpenAI

### Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/chatpdf.git
   cd chatpdf
   ```

2. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API da OpenAI:
   ```
   OPENAI_API_KEY=sua-chave-api-aqui
   ```

### Executando o Aplicativo

1. Inicie o aplicativo com o comando:
   ```
   streamlit run app.py
   ```

2. Acesse o aplicativo no seu navegador em `http://localhost:8501`

### Como Usar

1. Faça upload dos seus arquivos PDF pela barra lateral
2. Clique no botão "Iniciar Chatbot" para processar os documentos
3. Digite suas perguntas no campo de chat
4. Receba respostas baseadas no conteúdo dos seus documentos

## 📁 Estrutura do Projeto

```
chatpdf/
│
├── app.py              # Interface principal do aplicativo
├── backend.py          # Lógica de processamento de documentos e IA
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo
│
└── arquivos/           # Pasta onde os PDFs são armazenados (criada automaticamente)
```

## 📝 Requisitos

As principais dependências estão listadas no arquivo `requirements.txt`, incluindo:
- streamlit
- langchain
- langchain_community
- langchain_openai
- faiss-cpu (ou faiss-gpu para computadores com GPU)
- python-dotenv
- tiktoken

## ⚠️ Limitações

- Compatível apenas com arquivos PDF
- Requer conexão com a internet para acessar a API da OpenAI
- Tamanho máximo de documentos pode ser limitado pela memória disponível

## 📜 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.


---

Desenvolvido como parte do curso de Inteligência Artificial e Agentes IA
