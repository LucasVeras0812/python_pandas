import pandas as pd

data = {
    'Produto': ["Caderno", "Lápis", "Mochila"],
    'Preço': [20.5, 5.2, 90.1],
    'Quantidade': [5, 10, 3]
}

df = pd.DataFrame(data)
df['Total'] = df['Preço'] * df['Quantidade']
#print(df)
print()

df.rename(columns={'Produto': 'Item', 'Preço': "Valor"}, inplace=True)

#print(df)

filtro = df[df['Valor'] > 10] # filtrar linhas com base em condições
print(filtro)
print()

filtro2 = df[df['Valor'] > 10 & (df['Quantidade'] > 5)] # filtrar múltiplas condições (usando & para "e", usando | para "ou")
print(filtro2)
print()

ordenado = df.sort_values(by='Valor', ascending=False) # ordenar do mais caro para o mais barato
print(ordenado)