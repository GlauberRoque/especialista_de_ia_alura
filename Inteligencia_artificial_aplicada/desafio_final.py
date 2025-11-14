from openai import OpenAI


'''
Desafio final
1- carregar o arquivo .txt, onde cada linha será um elemento de uma lista
2- Manda-lá ao modelo que você está rodando para extrair, em formato JSON, onde cada item terá "usuário",'resenha original','resenha_pt','avaliacao'(positiva, negativa, neutra)
3- Transformar a resposta do modelo em uma lista de dicionários
4- criar uma função que, dada uma lista de dicionarios, percorre a lista e faz:
    - Conta a quantidade de avaliação positivas, negativa e neutras
    - une cada item dessa lista em uma variavel do tipo string com algum separador e retorna os dois
'''
#
client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="teste_ia",
)

resposta_do_llm = client_openai.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[{"role":"system", "content": "Você é um agente de IA prestativo."},
              {"role":"user", "content": "O que é IA Generativa?"}],
    temperature=1.0
)

print(resposta_do_llm.choices[0].message.content)