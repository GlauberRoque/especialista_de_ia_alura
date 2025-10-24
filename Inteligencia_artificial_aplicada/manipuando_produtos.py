import pandas as pd
import numpy as np

# Gerar dados fictícios
nomes_produtos = [f"Produto {i}" for i in range(1, 51)]
categorias = ["Eletrônicos", "Roupas", "Alimentos", "Livros", "Brinquedos"]
precos = np.round(np.random.uniform(10.0, 500.00, 50), 2)  # Preços entre 10 e 1000
quantidades_vendidas = np.random.randint(1, 500, 50)  # Quantidades entre 1 e 500
avaliacoes = np.round(np.random.uniform(1, 5, 50), 1)  # Avaliações entre 1.0 e 5.0

# Criar o DataFrame
df_produto = pd.DataFrame({
    "Nome do Produto": nomes_produtos,
    "Categoria do Produto": np.random.choice(categorias, 50),  # Escolher categorias aleatoriamente
    "Preço do Produto": precos,
    "Quantidade Vendida": quantidades_vendidas,
    "Avaliação do Produto": avaliacoes
})

# Exibir o DataFreme

print(df_produto['Categoria do Produto'].unique())

# Salvar em um arquivo CSV (opcional)
#df_produto.to_csv("produtos.csv", index=False, encoding="utf-8")