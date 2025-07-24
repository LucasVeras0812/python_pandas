import pandas as pd

data = {
    'Produto': ['Caderno', 'Caneta', 'Caneta', 'Borracha', 'Lápis', 'Lápis', None],
    'Valor': [12.5, 3.4, 3.4, 2.0, 1.5, None, 5.0],
    'Quantidade': [10, 50, 50, None, 100, 100, 20]
}

df_baguncado = pd.DataFrame(data)

# Verificando valores nulos
print(df_baguncado.isnull())
print()

# Preenchendo valores ausentes
df_baguncado['Produto'].fillna('Produto Desconhecido', inplace=True)
df_baguncado['Valor'].fillna(0, inplace=True)
df_baguncado['Quantidade'].fillna(0, inplace=True)

# Imprimindo resultado
print(df_baguncado)

# Salvando como Excel
df_baguncado.to_excel('produtos_limpos.xlsx', index=False)