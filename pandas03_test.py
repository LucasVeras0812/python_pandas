import pandas as pd

data = {
    'Produtos': ['Mochila', 'Caneta', 'Borracha', 'Pincel', 'Lancheira'],
    'Categoria': ['Mochilas', 'Papelaria', 'Papelaria', 'Papelaria', 'Mochilas'],
    'Valor': [80, 5, 3, 10, 40],
    'Quantidade': [2, 3, 3, 1, 2]
}

df = pd.DataFrame(data)
df['Total'] = df['Valor'] * df['Quantidade']
agrupado = df.groupby('Categoria').sum(numeric_only=True)
print(agrupado)
print()

filtro = df[df['Valor'] > 10]
print(filtro)
print()

do_maior_pro_menor = df.sort_values(by='Valor', ascending=False)
print(do_maior_pro_menor)