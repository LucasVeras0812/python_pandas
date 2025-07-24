import pandas as pd 

dados = {
    'Produto': ['Caderno', 'Caneta', 'Mochila'],
    'Preço': [12.5, 3.4, 89.9],
    'Quantidade': [10, 50, 5]
}

dado = pd.DataFrame(dados)
print(dado)