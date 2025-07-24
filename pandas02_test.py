import pandas as pd

data = {
    'Produto': ["Caderno", "Lápis", "Mochila"],
    'Preço': [20.5, 5.2, 90.1],
    'Quantidade': [5, 10, 3]
}

df = pd.DataFrame(data)
df['Total'] = df['Preço'] * df['Quantidade']
print(df)
print()

df.rename(columns={'Produto': 'Item', 'Preço': "Valor"}, inplace=True)

print(df)