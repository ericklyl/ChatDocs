# ChatDocs: Chat com Documentos (PDF, DOCX, TXT, PPTX)

## 1\. Visão Geral do Projeto

O ChatDocs é uma aplicação web interativa desenvolvida com **Streamlit** que permite aos usuários fazerem perguntas sobre o conteúdo de diversos tipos de documentos. Ele utiliza o poder das **Grandes Modelos de Linguagem (LLMs)** da OpenAI, orquestrados pelo framework **LangChain**, para processar documentos PDF, DOCX, TXT e PPTX.

**Funcionalidades Principais:**

  * **Upload de Documentos:** Carregue arquivos PDF, DOCX, TXT e PPTX diretamente pela interface.
  * **Processamento de Documentos:** Os documentos são divididos em pedaços menores (chunks) e convertidos em representações numéricas (embeddings).
  * **Armazenamento Vetorial:** Os embeddings são armazenados em um banco de dados vetorial FAISS para busca rápida de informações relevantes.
  * **Chat Inteligente:** Converse com seus documentos, fazendo perguntas e obtendo respostas baseadas no conteúdo carregado.
  * **Memória Conversacional:** O chatbot mantém o contexto da conversa, permitindo diálogos mais fluidos e coerentes.

-----

## 2\. Tecnologias Utilizadas

Este projeto foi desenvolvido em Python e faz uso das seguintes bibliotecas e ferramentas:

  * **Python 3.11.9** (versão utilizada no desenvolvimento e recomendada)
  * **Streamlit**: Para a interface web interativa.
  * **LangChain**: Framework essencial para construção de aplicações com LLMs.
  * **OpenAI API**: Fornece os modelos de linguagem (GPT-3.5-turbo-0125) e de embeddings.
  * **FAISS**: Para armazenamento e busca eficiente de vetores de documentos.
  * **python-dotenv**: Para o gerenciamento seguro das chaves de API via arquivo `.env`.
  * **pypdf**: Para o carregamento de arquivos PDF.
  * **docx2txt**: Para o carregamento de arquivos DOCX.
  * **python-pptx**: Para o carregamento de arquivos PPTX.

-----

## 3\. Estrutura do Projeto

A estrutura de diretórios do projeto é a seguinte:

```
ChatDocs-main/
└── ChatPDF/             # Esta é a pasta raiz do projeto após clonar/descompactar
    ├── arquivos/               # Pasta para armazenar os documentos carregados pelo usuário.
    │   └── (documentos .pdf, .docx, .txt, .pptx)
    ├── venv/                   # Ambiente virtual Python (IGNORADO PELO GIT)
    ├── .env                    # Arquivo para variáveis de ambiente (será fornecido)
    ├── app.py                  # Script principal da interface do usuário Streamlit.
    ├── backend.py              # Lógica de processamento de documentos e do chatbot.
    ├── requirements.txt        # Lista de dependências Python do projeto.
    └── README.md               # Documentação do projeto (este arquivo).
```

-----

## 4\. Configuração do Ambiente

Siga os passos abaixo para configurar o projeto na sua máquina:

### 4.1. Pré-requisitos

  * **Python 3.11.x**: Certifique-se de ter o Python 3.11.9 (ou uma versão 3.11.x compatível) instalada. Você pode baixar em [python.org](https://www.python.org/downloads/).
  * **Git**: Para clonar o repositório (opcional, mas recomendado). Baixe em [git-scm.com](https://git-scm.com/downloads).

### 4.2. Configuração do Projeto

1.  **Clone o Repositório:**

    ```bash
    git clone https://github.com/ericklyl/ChatDocs.git
    cd ChatDocs
    ```

    *Se você baixou um ZIP, descompacte-o e abra o terminal na pasta raiz do projeto (`ChatDocs-main/ChatPDF/`).*

2.  **Navegue até a pasta `ChatPDF` (Pasta Raiz do Projeto):**
    É **essencial** que todos os comandos seguintes sejam executados **dentro da pasta `ChatPDF`**.

    ```bash
    cd ChatPDF
    ```

    Sua linha de comando deve indicar que você está neste diretório, por exemplo: `C:\Caminho\Para\ChatDocs-main\ChatPDF>`

3.  **Crie um Ambiente Virtual:**
    É **fundamental** usar um ambiente virtual para isolar as dependências do projeto e evitar conflitos. Certifique-se de estar na pasta `ChatPDF` antes de executar este comando.

    ```bash
    python -m venv venv
    ```

4.  **Ative o Ambiente Virtual:**

      * Certifique-se de estar dentro da pasta `ChatPDF`.
      * No **Windows PowerShell/CMD**:
        ```bash
        .\venv\Scripts\activate
        ```
      * No **Linux/macOS**:
        ```bash
        source venv/bin/activate
        ```
      * Você verá `(venv)` no início da linha do seu terminal, indicando que o ambiente está ativo. **Este é um passo CRÍTICO e deve ser feito sempre antes de instalar ou rodar o projeto.**

5.  **Instale as Dependências Python:**
    Com o ambiente virtual **ativo** e ainda na pasta `ChatPDF`, instale todas as bibliotecas listadas no `requirements.txt`.

    ```bash
    pip install -r requirements.txt
    ```

    **ATENÇÃO:** Monitore o terminal para quaisquer mensagens de erro durante a instalação.

6.  **Configure sua Chave da API da OpenAI:**

      * **O arquivo `.env` contendo a chave da API da OpenAI será fornecido junto com o projeto.**
      * Ele sera enviado pro professor a parte pois é perigoso fornecer a chave via github
-----

## 5\. Como Executar o Aplicativo

Após configurar o ambiente e instalar todas as dependências:

1.  **Abra seu terminal** (PowerShell, CMD, ou Git Bash).
2.  **Navegue até a pasta `ChatPDF`** (a pasta raiz do seu projeto):
    ```bash
    cd C:\Users\SeuUsuario\Downloads\ChatDocs-main\ChatPDF # Exemplo de caminho
    ```
3.  **Ative o Ambiente Virtual:**
    ```bash
    .\venv\Scripts\activate
    ```
    Você deve ver `(venv)` no prompt.
4.  **Adicione seus Documentos:** Coloque seus arquivos (PDF, DOCX, TXT, PPTX) na pasta `ChatPDF/arquivos/`. Você também pode carregá-los pela interface do Streamlit.
5.  **Execute o Aplicativo Streamlit:**
    ```bash
    streamlit run app.py
    ```
    O aplicativo abrirá automaticamente no seu navegador web (geralmente em `http://localhost:8501`).

-----

## 6\. Solução de Problemas Comuns (e o que enfrentamos\!)

Esta seção lista os erros mais frequentes que podem ocorrer durante a configuração ou execução, e suas soluções, baseadas nos desafios que encontramos durante o desenvolvimento.

### 6.1. Erro: `'streamlit' não é reconhecido` ou `'activate' não é reconhecido`

```
'streamlit' não é reconhecido como nome de cmdlet...
.\venv\Scripts\activate : O termo '.\venv\Scripts\activate' não é reconhecido...
```

  * **Causa:** O ambiente virtual não está ativado, ou as bibliotecas não foram instaladas nele.
  * **Solução:**
    1.  Certifique-se de que você está no diretório correto (`ChatPDF/`).
    2.  Verifique se `(venv)` aparece no seu prompt. Se não, ative o ambiente virtual usando `.\venv\Scripts\activate`.
    3.  Se a ativação falhar, prossiga para a Seção 6.2 (Problemas de Política de Execução).
    4.  Com o `venv` ativo, execute `pip install -r requirements.txt` novamente para garantir que todas as dependências foram instaladas.

-----

### 6.2. Erro: `A execução de scripts foi desabilitada neste sistema` (PowerShell)

```
.\venv\Scripts\activate : O arquivo [...]Activate.ps1 não pode ser carregado porque a execução de scripts foi desabilitada neste sistema.
```

  * **Causa:** O PowerShell, por padrão, impede a execução de scripts locais por segurança.
  * **Solução:**
    1.  **Abra o PowerShell como Administrador:** Clique com o botão direito no menu Iniciar \> "Windows PowerShell (Admin)".
    2.  Execute o comando: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
    3.  Digite `S` e pressione Enter para confirmar.
    4.  **Feche o PowerShell de Administrador** e abra um **novo PowerShell normal**. Tente ativar o ambiente virtual novamente.

-----

### 6.3. Erro: `openai.OpenAIError: The api_key client option must be set`

```
openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable
```

  * **Causa:** O aplicativo não consegue encontrar sua chave da API da OpenAI.
  * **Solução:**
    1.  Verifique se o arquivo `.env` está na pasta **raiz do projeto** (`ChatPDF/`).
    2.  Confirme que o `.env` contém a linha `OPENAI_API_KEY="SUA_CHAVE_DA_API_DA_OPENAI_AQUI"` com uma chave válida.
    3.  **Reinicie o aplicativo Streamlit** (pare com `Ctrl + C` e rode `streamlit run app.py` novamente) após qualquer alteração.

-----

### 6.4. Erro: `ModuleNotFoundError: No module named 'textblob'`

  * **Causa:** A biblioteca `textblob` está faltando, ou o código de análise de sentimento não foi completamente removido.
  * **Solução:**
    1.  Certifique-se de que o código de análise de sentimento foi **removido completamente** do `app.py` (verifique visualmente).
    2.  **Remova `textblob` do `requirements.txt`** se ainda estiver lá.
    3.  No terminal (com `venv` ativo): `pip uninstall textblob` (se estiver instalado) e depois `pip install -r requirements.txt`.

-----

### 6.5. Erro: `ModuleNotFoundError: No module named 'docx2txt'` ou `ModuleNotFoundError: No module named 'pptx'` (ou outros loaders)

  * **Causa:** As bibliotecas `docx2txt` ou `python-pptx` (ou suas dependências) não estão instaladas corretamente.
  * **Solução:**
    1.  **Ative o ambiente virtual** (`.\venv\Scripts\activate`).
    2.  **Reinstale especificamente a biblioteca faltante:**
          * Para `docx2txt`: `pip install docx2txt --force-reinstall`
          * Para `python-pptx`: `pip install python-pptx --force-reinstall`
    3.  Verifique se a instalação foi bem-sucedida usando `pip show [nome_da_biblioteca]`.

-----
