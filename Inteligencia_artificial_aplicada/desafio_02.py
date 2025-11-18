import os
import google.generativeai as genai # pip install google-generative-ai
import pandas as pd
import chardet 
import numpy as np
'''
DESAFIO 2
1- Carregar um arquivo .csv com feedback de clientes (review.csv)
2- Usar um LLM para classificar o sentimento de cada feedback
3- adicionar uma nava coluna com essa classificação ao DataFrame
'''
#Configurando a LLM
genai.configure(api_key="***********************") # Substitua pela sua chave de API
model = genai.GenerativeModel("gemini-2.5-flash")# Definindo o modelo da IA
chat = model.start_chat() # Inicializando um chat

#Leitura do Arquivo
df_reviews = pd.read_csv("Arquivo/reviews.csv")

#Separando apenas a coluna que importa para a LLM
coluna_de_reviews = df_reviews["reviewText"]
#print(coluna_de_reviews)

#criando uma lista de analise de sentimentos
lista_analise_sentimentos = []

#Laço FOR para interar por cada linha e enviar a LLM para serem avaliadas
for review_numero, resenha in enumerate(coluna_de_reviews):
    resposta = chat.send_message(f"""Você irá analisar a resenha que te enviarei, e retorna com uma análise de sentimento. 
                                 você deve responder APENAS com uma das seguintes palavras: 'Positiva', 'Negativa' ou 'Neutra',
                                 indicando o sentimento relativo aquea resenha específica
                                 segue a resenha a ser analisada: {resenha}""") # define o prompt para a IA
    lista_analise_sentimentos.append(resposta.text)
    #print(f'Resenha {review_numero}: {resenha} --> Sentimento: {resposta.text}')
    
#Adicionando nova COLUNA

df_reviews['Análise de Sentimentos'] = lista_analise_sentimentos
