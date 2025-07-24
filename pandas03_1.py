import pandas as pd

data = {
    'Item': ['Caderno', 'Lápis', 'Mochila', 'Caneta', 'Borracha'],
    'Categoria': ['Papelaria', 'Papelaria', 'Mochilas', 'Papelaria', 'Papelaria'],
    'Valor': [20.5, 5.2, 90.1, 2.5, 1.8],
    'Quantidade': [5, 10, 3, 20, 15]    
}

df = pd.DataFrame(data)
df['Total'] = df['Valor'] * df['Quantidade']

#Agrupamento
agrupado = df.groupby('Categoria').sum(numeric_only=True)
print(agrupado)
print()

#Estatísticas Básicas
print(df['Valor'].mean()) # Média
print(df['Quantidade'].max()) # Maior valor
print(df['Total'].sum()) # Soma total