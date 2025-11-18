from openai import OpenAI
import json
from contato_llm import recebe_linha

'''
Desafio final
1- carregar o arquivo .txt, onde cada linha será um elemento de uma lista
2- Manda-lá ao modelo que você está rodando para extrair, em formato JSON, onde cada item terá "usuário",'resenha original','resenha_pt','avaliacao'(positiva, negativa, neutra)
3- Transformar a resposta do modelo em uma lista de dicionários
4- criar uma função que, dada uma lista de dicionarios, percorre a lista e faz:
    - Conta a quantidade de avaliação positivas, negativa e neutras
    - une cada item dessa lista em uma variavel do tipo string com algum separador e retorna os dois
'''


lista_resenhas = []
#Leitura do arquivo
with open("Arquivo/Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_resenhas.append(linha.strip())
        
#Chama a função que vai retornar um JSON preparado pela LLM e transforma em dicionario
lista_resenhas_json = []
for resenha in lista_resenhas:
    resenha_json = recebe_linha(resenha)
    # Verificar se a resposta não está vazia
    if not resenha_json.strip():
        print(f"Erro: Resposta vazia para a resenha: {resenha}")
        continue  # Pula para a próxima resenha
    
    # Remover cabeçalhos ou rodapés como ```json e ```
    resenha_json = resenha_json.strip("```json").strip("```").strip()
    
    try:
        resenha_dict = json.loads(resenha_json)
        lista_resenhas_json.append(resenha_dict)
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON para a resenha: {resenha}")
        print(f"Resposta recebida: {resenha_json}")
        print(f"Erro: {e}")
    
#print(lista_resenhas_json)    

def Contador_e_juntador(lista_de_dicionarios):
    contador_positiva = 0
    contador_negativa = 0
    contador_neutra = 0
    lista_de_dicionarios_str = []
    
    for item in lista_de_dicionarios:
        
        if item['avaliacao'] == "positiva":
            contador_positiva += 1
        elif item['avaliacao'] == "negativa":
            contador_negativa += 1
        elif item['avaliacao'] == "neutra":
            contador_neutra += 1
        
        lista_de_dicionarios_str.append(str(item))
        
    textos_unidos = "#####".join(lista_de_dicionarios_str)
    return contador_positiva, contador_negativa, contador_neutra, textos_unidos

pos, neg, neut, textos = Contador_e_juntador(lista_resenhas_json)
print(f"Positivas: {pos}\n")
print(f"Negativas: {neg}\n")
print(f"Neutras: {neut}\n")
print(f"Textos: {textos}\n")
