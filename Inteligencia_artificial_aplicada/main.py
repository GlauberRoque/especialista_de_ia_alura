import os
import google.generativeai as genai # pip install google-generative-ai

genai.configure(api_key="AIzaSyDxlO9iILrbpAFwTapaCYM-wHQCd2KFlR8") # Substitua pela sua chave de API

model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat()

prompt = input("Digite o seu prompt: ")# vai receber o prompt do usuário

#loop para continuar a conversa
while prompt != "sair":
    response = chat.send_message(prompt)
    print("Gemini: ", response.text)
    prompt = input("Você: ")
    
print("----- Conversa encerrada -----")


