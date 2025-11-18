from openai import OpenAI

#Configurando o Agent IA
client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="teste_ia",
)

def recebe_linha(linha):
    resposta_do_llm = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[{"role":"system", "content": """Você é um em analise de dados e conversão para JSON.
                   Você recebera uma linha de texto que é uma resenha de um aplicativo em um marktplace online, é importante que não retorne nada alem do json.
                   Quero que você analise essa resenha, e me retorne um Json com as seguintes chaves:
                   - 'usuario': o nome do usuário que fez a resenha
                   - 'resenha_original: a resenha no idioma original que você recebeu
                   - 'resenha_pt: a resenha traduzida para o português (pt-br)
                   - 'avaliacao': uma avaliação se a resenha foi: 'Positiva', 'Negativa' ou 'Neutra'
                   exemplo:
                   {
                    "usuario": "Safoan Riyad",
                    "resenha_original": "53409593$Safoan Riyad$J'aimais bien ChatGPT. Mais la dernière mise à jour a tout gâché. Elle a tout oublié.",
                    "resenha_pt": "Amo o ChatGPT! A última atualização deixou tudo esquecido.",
                    "avaliacao": "Positiva"
                    }
                    
                   """},
                {"role":"user", "content": f"Resenha: {linha}"}],
        temperature=0.0
    )
    print(resposta_do_llm.choices[0].message.content)
    return resposta_do_llm.choices[0].message.content