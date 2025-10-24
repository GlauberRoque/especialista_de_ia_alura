import os
import google.generativeai as genai # pip install google-generative-ai

genai.configure(api_key="AIzaSyDxlO9iILrbpAFwTapaCYM-wHQCd2KFlR8") # Substitua pela sua chave de API
model = genai.GenerativeModel("gemini-2.5-flash")# Definindo o modelo da IA
chat = model.start_chat() # Inicializando um chat

emails = [
    """Olá,
    
    Gostaria de compartilhar algumas novidades e informações interessantes sobre tecnologia. Este é um assunto que tem despertado bastante interesse recentemente e acredito que você vai gostar do conteúdo.
    
    Atenciosamente,
    Equipe Tecnologia""",

    """Olá,

    Gostaria de compartilhar algumas novidades e informações interessantes sobre saúde. Este é um assunto que tem despertado bastante interesse recentemente e acredito que você vai gostar do conteúdo.

    Atenciosamente,
    Equipe Saúde""",

    """Olá,

    Gostaria de compartilhar algumas novidades e informações interessantes sobre educação. Este é um assunto que tem despertado bastante interesse recentemente e acredito que você vai gostar do conteúdo.

    Atenciosamente,
    Equipe Educação""",

    """Olá,

    Gostaria de compartilhar algumas novidades e informações interessantes sobre esportes. Este é um assunto que tem despertado bastante interesse recentemente e acredito que você vai gostar do conteúdo.

    Atenciosamente,
    Equipe Esportes""",

    """Olá,

    Gostaria de compartilhar algumas novidades e informações interessantes sobre finanças. Este é um assunto que tem despertado bastante interesse recentemente e acredito que você vai gostar do conteúdo.

    Atenciosamente,
    Equipe Finanças""",

    """Olá,

    Gostaria de compartilhar algumas novidades e informações interessantes sobre viagens. Este é um assunto que tem despertado bastante interesse recentemente e acredito que você vai gostar do conteúdo.

    Atenciosamente,
    Equipe Viagens""",

    """Olá,

    Gostaria de compartilhar algumas novidades e informações interessantes sobre culinária. Este é um assunto que tem despertado bastante interesse recentemente e acredito que você vai gostar do conteúdo.

    Atenciosamente,
    Equipe Culinária""",

    """Olá,

    Gostaria de compartilhar algumas novidades e informações interessantes sobre moda. Este é um assunto que tem despertado bastante interesse recentemente e acredito que você vai gostar do conteúdo.

    Atenciosamente,
    Equipe Moda""",

    """Olá,

    Gostaria de compartilhar algumas novidades e informações interessantes sobre música. Este é um assunto que tem despertado bastante interesse recentemente e acredito que você vai gostar do conteúdo.

    Atenciosamente,
    Equipe Música""",

    """Olá,

    Gostaria de compartilhar algumas novidades e informações interessantes sobre cinema. Este é um assunto que tem despertado bastante interesse recentemente e acredito que você vai gostar do conteúdo.

    Atenciosamente,
    Equipe Cinema"""
]
#FUNÇÃO para resumir o EMAIL
def resumir_emails(lista_de_emails):
    lista_de_resumos = []
    for numero, email in enumerate(lista_de_emails):# Varre e enumera os emails dentro da lista
        resposta = chat.send_message(f"vou te mandar um corpo de um email, resuma ele para mim em apenas 1 linha, segue o email: {email}") # define o prompt para a IA
        #print(f'E-mail {numero + 1}: {resposta.text}')
        lista_de_resumos.append(f'E-mail {numero + 1}: {resposta.text}')
        #print("-" * 100)
        
    return lista_de_resumos

lista_resumos = resumir_emails(emails)       

with open("Arquivo/lista-de-resumos.txt", "a", encoding="utf-8") as arquivo:
    for resumo in lista_resumos:
        arquivo.write(f'{resumo} \n')