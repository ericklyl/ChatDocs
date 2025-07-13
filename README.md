# ChatDocs: Chat com Documentos

## 1\. Título do Projeto e Integrantes

**Título do Projeto:** ChatDocs: Chat com Documentos

**Integrantes:**

  * Erick Loyola
  * Lara Aguilar
  * Renzo Avance
  * Rodolfo Oliveira


-----

## 2\. Objetivo Geral do Sistema

O ChatDocs é uma aplicação web interativa desenvolvida para facilitar a interação com o conteúdo de diversos tipos de documentos. Seu objetivo principal é permitir que os usuários façam perguntas em linguagem natural e recebam respostas precisas e contextualizadas, extraídas diretamente de seus próprios arquivos. Isso é alcançado através da integração de Modelos de Linguagem de Grande Escala (LLMs) com um sistema de recuperação de informações baseado em embeddings, transformando coleções de documentos em uma base de conhecimento conversacional.


-----

## 3\. Tecnologias e Bibliotecas Utilizadas

Este projeto foi desenvolvido em **Python 3.11.9** e faz uso das seguintes bibliotecas e ferramentas:

  * **Streamlit**: Framework de código aberto para a criação rápida de interfaces web interativas em Python. Utilizado para construir a interface de usuário do chatbot.
  * **LangChain**: Framework flexível para o desenvolvimento de aplicações alimentadas por LLMs. Essencial para orquestrar o pipeline do chatbot, incluindo o carregamento de documentos, divisão de texto, criação de embeddings, gerenciamento de memória e interação com o LLM.
  * **OpenAI API**: Interface de programação de aplicações da OpenAI, utilizada para:
      * **Modelos de Linguagem (LLM):** `gpt-3.5-turbo-0125` para gerar as respostas do chatbot.
      * **Modelos de Embeddings:** `OpenAIEmbeddings` para converter texto em vetores numéricos.
  * **FAISS**: (Facebook AI Similarity Search) Uma biblioteca para busca eficiente de similaridade. Utilizada como banco de dados vetorial em memória para armazenar os embeddings dos documentos e permitir a recuperação rápida de trechos relevantes.
  * **python-dotenv**: Para o gerenciamento seguro das variáveis de ambiente (como a chave da API da OpenAI) carregando-as de um arquivo `.env`.
  * **pypdf**: Biblioteca Python para trabalhar com arquivos PDF, utilizada para extrair texto de documentos PDF.
  * **docx2txt**: Biblioteca Python para extrair texto de arquivos Microsoft Word (`.docx`).
  * **python-pptx**: Biblioteca Python para ler e manipular arquivos Microsoft PowerPoint (`.pptx`), utilizada para extrair o texto dos slides.



-----

## 4\. Requisitos para Execução

Para executar o projeto ChatDocs, você precisará do seguinte ambiente:

  * **Python 3.11.x**: Recomenda-se a versão **Python 3.11.9**.
      * Verifique sua versão com: `python --version`
      * Baixe e instale o Python em: [python.org](https://www.python.org/downloads/)
  * **Git**: Recomendado para clonar o repositório.
      * Verifique sua instalação com: `git --version`
      * Baixe e instale em: [git-scm.com](https://git-scm.com/downloads)
  * **Chave da API da OpenAI**: O projeto requer uma chave válida da API da OpenAI.
      * Obtenha em: [platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)


-----

## 5\. Instruções Passo a Passo para Instalação e Execução

Siga cuidadosamente estas instruções para configurar e rodar o projeto ChatDocs em sua máquina:

### 5.1. Clonar o Repositório

Abra seu terminal (PowerShell, CMD, Git Bash) e clone o repositório do GitHub:

```bash
git clone https://github.com/ericklyl/ChatDocs.git
```

Isso criará uma pasta chamada `ChatDocs`.

### 5.2. Navegar para a Pasta Raiz do Projeto

Entre na pasta `ChatDocs` que contém o subdiretório `ChatPDF`. Em seguida, entre na pasta `ChatPDF`. **É crucial que todos os comandos seguintes sejam executados DENTRO desta pasta `ChatPDF`**.

```bash
cd ChatDocs
cd ChatPDF
```

Seu prompt de comando deve agora indicar que você está no diretório `ChatPDF`, por exemplo: `C:\Users\SeuUsuario\Downloads\ChatDocs\ChatPDF>`

### 5.3. Criar o Ambiente Virtual

Dentro da pasta `ChatPDF` (confirme seu prompt\!), crie um ambiente virtual para isolar as dependências:

```bash
python -m venv venv
```

Isso criará uma nova pasta `venv` dentro de `ChatPDF`.

### 5.4. Ativar o Ambiente Virtual

Ainda dentro da pasta `ChatPDF`, ative o ambiente virtual.

  * **No Windows PowerShell/CMD:**

    ```bash
    .\venv\Scripts\activate
    ```

  * **No Linux/macOS:**

    ```bash
    source venv/bin/activate
    ```

Você deve ver `(venv)` no início da linha do seu terminal. Isso significa que o ambiente está ativo e todos os `pip install` e `streamlit run` serão executados dentro dele.

### 5.5. Instalar as Dependências Python

Com o ambiente virtual **ativo** (`(venv)` no prompt\!), instale todas as bibliotecas listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Monitorar a Saída:** Observe atentamente o terminal durante este processo. Se houver mensagens de `ERROR:` ou `Failed building wheel for...`, isso indica que alguma dependência não foi instalada corretamente.

### 5.6. Configurar a Chave da API da OpenAI

1.  O arquivo `.env` (que contém a chave da API da OpenAI) **será fornecido junto com o projeto**. Certifique-se de que ele esteja na pasta **`ChatPDF/`** (a pasta raiz do seu projeto).
2.  **Verifique o conteúdo do `.env`:** Abra-o com um editor de texto simples (como Bloco de Notas). Ele deve conter sua chave da API no formato:
    ```
    OPENAI_API_KEY="SUA_CHAVE_DA_API_DA_OPENAI_AQUI"
    ```
    Substitua `"SUA_CHAVE_DA_API_DA_OPENAI_AQUI"` pela chave real, que começa com `sk-`.
3. Quando voce baixar o arquivo.env, pode ser que ele venha sem o "." antes do env, renomeie ele para colocar o ponto e ficar como ".env"

### 5.7. Adicionar Documentos

Use a pasta chamada `files` dentro de `ChatPDF/` se ela ainda não existir. Coloque seus arquivos PDF, DOCX, TXT e PPTX com os quais deseja conversar dentro desta pasta `ChatPDF/files/`. Alternativamente, você poderá fazer o upload pela própria interface do Streamlit.

### 5.8. Executar o Aplicativo

Com o ambiente virtual **ativo** e na pasta `ChatPDF/`, execute o Streamlit:

```bash
streamlit run app.py
```

O aplicativo será aberto automaticamente no seu navegador web (geralmente em `http://localhost:8501`).



-----

## 6\. Demonstração das Principais Funcionalidades

### 6.1. Interface de Carregamento e Inicialização

Ao abrir o aplicativo, você verá a interface principal do chat e uma barra lateral para carregar documentos.

1.  **Carregar Documentos:** Use o "Carregue seus arquivos (PDF, DOCX, TXT, PPTX)" para fazer upload. Os arquivos serão salvos na pasta `files/`.
2.  **Arquivos Carregados:** A lista abaixo do uploader mostrará os documentos detectados na pasta `files/`.
3.  **Iniciar Chatbot:** Clique no botão "Iniciar Chatbot" para processar os documentos. Uma barra de progresso indicará o status.

### 6.2. Interagindo com o Chatbot

Após a inicialização bem-sucedida, a interface do chat estará pronta.

1.  **Histórico da Conversa:** As suas perguntas e as respostas do chatbot aparecerão aqui.
2.  **Campo de Pergunta:** Digite sua pergunta sobre o conteúdo dos documentos no campo "Digite sua pergunta aqui".
3.  **Respostas:** O chatbot gerará uma resposta baseada nos documentos e no histórico da conversa.

**Exemplo de uso:**

  * **Pergunta:** "O que é o projeto artemis?"
  * **Resposta:** Uma resposta contextualizada baseada nos documentos fornecidos será exibida.



-----

## 7\. Possíveis Limitações e Sugestões de Melhorias Futuras

### 7.1. Limitações Atuais

  * ** Dependência da qualidade do documentode entrada
  * ** Custo associado ao uso de LLM sem larga escala
  * ** Possível latência na geração de respostas
  * ** Questões de privacidade e segurança com dados sensíveis


### 7.2. Sugestões de Melhorias Futuras

  * ** Suporte a Múltiplos Formatos (Expandirpara XLSX, HTML, XML)
  * ** Interface Conversacional Aprimorada (Incorporar histórico e memória de longo prazo)
  * **  Otimização de Desempenho (Técnicas avançadas de retrieval)

-----
