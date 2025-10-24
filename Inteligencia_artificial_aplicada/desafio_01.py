import pandas as pd
import chardet 
import os
import google.generativeai as genai # pip install google-generative-ai

genai.configure(api_key="AIzaSyDxlO9iILrbpAFwTapaCYM-wHQCd2KFlR8") # Substitua pela sua chave de API
model = genai.GenerativeModel("gemini-2.5-flash")# Definindo o modelo da IA
chat = model.start_chat() # Inicializando um chat

'''
DESAFIO:
    1- CRIAR UM ARQUIVO .TXT A PARTIR DE UMA LISTA DE PERGUNTAS VINDAS DE UMA LISTA EM PYTHON.
    2- LER AS PERGUNTAS DO ARQUIVO .TXT
    3- OBTER RESPOSTAS DE UMA LLM PARA CADA PERGUNTA
    4- SALVAR OS RESULTADOS EM UM NOVO ARQUIVO .CSV
'''

lista_de_perguntas = [
    "O que é RPA e quais são seus principais benefícios para as empresas?",
    "Quais tipos de processos são mais adequados para automação com RPA?",
    "Qual a diferença entre RPA atendido (attended) e não atendido (unattended)?",
    "Quais são os principais desafios na implementação de uma solução de RPA?",
    "Como o RPA se diferencia de outras formas de automação, como scripts ou macros?",
    "Quais ferramentas de RPA são mais usadas hoje em dia?",
    "Como você lida com exceções e erros em um processo automatizado com RPA?",
    "Quais boas práticas você recomenda ao desenvolver um robô de RPA?",
    "Como garantir a segurança e conformidade em processos automatizados com RPA?",
    "Dá para integrar RPA com APIs ou sistemas como SAP, SharePoint ou bancos de dados? "
    ]
# CRIANDO UM ARQUIVO TXT COM OS DADOS DAS PERGUNTAS SALVAS NA LISTA 
with open("Arquivo/perguntas.txt", "w", encoding="utf-8") as arquivo:
    for pergunta in lista_de_perguntas:
        arquivo.write(pergunta + "\n")
        
# LER PERGUNTAS DO ARQUIVO.TXT
lista_desafio = []
with open("Arquivo/perguntas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_desafio.append(linha.strip())
        
# OBTER RESPOSTAS DA LLM PARA CADA PERGUNTA
lista_dicionario_perguntas = []

for pergunta in lista_desafio:
    resposta = chat.send_message(f'Gere uma resposta sucinta para a pergunta: {pergunta}')
    resposta_texto = resposta.text
    resposta_limpa = resposta_texto.replace('*', '').replace('\n', '')
    lista_dicionario_perguntas.append({"pergunta":pergunta, "resposta":resposta_limpa})

#print(lista_dicionario_perguntas)   

# SALVAR OS RESULTADOS EM UM NOVO ARQUIVO .CSV USANDO PANDAS
df_perguntas_e_respostas = pd.DataFrame(lista_dicionario_perguntas)
df_perguntas_e_respostas.to_csv("Arquivo/resposta.csv", index=False, encoding='utf-8')
#print(df_perguntas_e_respostas)

# LER O ARQUIVO .CSV USANDO PANDAS.
        