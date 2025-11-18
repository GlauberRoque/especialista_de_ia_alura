# Projeto de Inteligência Artificial Aplicada

Este projeto utiliza ferramentas de inteligência artificial e manipulação de dados para realizar diversas tarefas, como análise de sentimentos, resumo de e-mails, manipulação de dados com Pandas, e muito mais.

## Estrutura do Projeto

O projeto está dividido em vários arquivos Python, cada um responsável por uma funcionalidade específica:

### 1. **`main.py`**
- Configura e inicializa o modelo **Gemini 2.5 Flash** da API do Google Generative AI.
- Permite interações com o modelo em um loop de conversa.

### 2. **`resumir_emails.py`**
- Resumo de e-mails utilizando a API do Google Generative AI.
- Lê uma lista de e-mails, envia para a IA e salva os resumos em um arquivo de texto.

### 3. **`desafio_02.py`**
- Classifica o sentimento de feedbacks de clientes.
- Lê um arquivo CSV com feedbacks, utiliza a IA para análise de sentimentos e adiciona uma nova coluna ao DataFrame com os resultados.

### 4. **`manipulando_dados_pandas.py`**
- Manipula dados utilizando a biblioteca **Pandas**.
- Detecta automaticamente o encoding de um arquivo CSV utilizando a biblioteca **chardet**.
- Lê o arquivo CSV com o encoding correto e exibe os dados.

### 5. **`manipuando_produtos.py`**
- Gera um DataFrame fictício com informações de produtos.
- Inclui colunas como nome do produto, categoria, preço, quantidade vendida e avaliação.
- Permite salvar os dados gerados em um arquivo CSV.

### 6. **`desafio_final.py`**
- Realiza uma tarefa final utilizando a API OpenAI.
- Processa resenhas de usuários, traduz e analisa os dados, e retorna os resultados em formato JSON.

### 7. **`contato_llm.py`**
- Configura o cliente para se conectar a um servidor local de LLM (Large Language Model).
- Define funções auxiliares para enviar e receber dados da IA.

---

## Requisitos

- Python 3.8 ou superior
- Bibliotecas necessárias (instale com `pip`):
  - `pandas`
  - `numpy`
  - `# Projeto de Inteligência Artificial Aplicada

Este projeto utiliza ferramentas de inteligência artificial e manipulação de dados para realizar diversas tarefas, como análise de sentimentos, resumo de e-mails, manipulação de dados com Pandas, e muito mais.

## Estrutura do Projeto

O projeto está dividido em vários arquivos Python, cada um responsável por uma funcionalidade específica:

### 1. **`main.py`**
- Configura e inicializa o modelo **Gemini 2.5 Flash** da API do Google Generative AI.
- Permite interações com o modelo em um loop de conversa.

### 2. **`resumir_emails.py`**
- Resumo de e-mails utilizando a API do Google Generative AI.
- Lê uma lista de e-mails, envia para a IA e salva os resumos em um arquivo de texto.

### 3. **`desafio_02.py`**
- Classifica o sentimento de feedbacks de clientes.
- Lê um arquivo CSV com feedbacks, utiliza a IA para análise de sentimentos e adiciona uma nova coluna ao DataFrame com os resultados.

### 4. **`manipulando_dados_pandas.py`**
- Manipula dados utilizando a biblioteca **Pandas**.
- Detecta automaticamente o encoding de um arquivo CSV utilizando a biblioteca **chardet**.
- Lê o arquivo CSV com o encoding correto e exibe os dados.

### 5. **`manipuando_produtos.py`**
- Gera um DataFrame fictício com informações de produtos.
- Inclui colunas como nome do produto, categoria, preço, quantidade vendida e avaliação.
- Permite salvar os dados gerados em um arquivo CSV.

### 6. **`desafio_final.py`**
- Realiza uma tarefa final utilizando a API OpenAI.
- Processa resenhas de usuários, traduz e analisa os dados, e retorna os resultados em formato JSON.

### 7. **`contato_llm.py`**
- Configura o cliente para se conectar a um servidor local de LLM (Large Language Model).
- Define funções auxiliares para enviar e receber dados da IA.

