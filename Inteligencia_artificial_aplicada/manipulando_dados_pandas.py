import pandas as pd
import chardet 

#Encontra o tipo do enconding do ARQUIVO
with open('Arquivo/nomes_medias.csv', 'rb') as f:
    result = chardet.detect(f.read())
    print(result)


df = pd.read_csv('Arquivo/nomes_medias.csv', encoding=result['encoding'])# Ler o csv que passamos como parametro e pega o encoding para não dar erro
print(df)