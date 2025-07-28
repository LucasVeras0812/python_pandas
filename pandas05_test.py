import pandas as pd

produtos = pd.DataFrame({
    'ID': [1, 2 , 3],
    'Produto': ['Lápis', 'Borracha', 'Mochila'],
    'Preço': [5, 3, 20]
})

quantidade = pd.DataFrame({
    'ID': [1, 2 , 3],
    'Quantidade': [20, 30, 10]
})

res = pd.merge(produtos, quantidade, on='ID')

res['Total'] = res.apply(lambda linha: linha['Preço'] * linha['Quantidade'], axis=1)
print(res)
print()

ordenado = res.sort_values(by='Total', ascending=False)
print(ordenado)
