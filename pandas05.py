import pandas as pd

# merge() — Juntar DataFrames (tipo SQL)
# O merge() é usado para juntar dois DataFrames com base em uma ou mais colunas.

produtos = pd.DataFrame({
    'ID': [1, 2, 3],
    'Produto': ['Caderno', 'Caneta', 'Lápis']
})

estoque = pd.DataFrame({
    'ID': [1, 2, 3],
    'Quantidade': [100, 200, 150]
})

resultado = pd.merge(produtos, estoque, on='ID')
print(resultado)
print()
# também aceita how='left', how='right', how='outer' (como JOINs em SQL).
###########################################################################

#concat() — Concatenar DataFrames
# usado para empilhar DataFrames vertical ou horizontalmente.

df1 = pd.DataFrame({
    'Produto': ['Caderno', 'Caneta'],
    'Preço': [10,2]
})

df2 = pd.DataFrame({
    'Produto': ['Lápis', 'Borracha'],
    'Preço': [1.5, 0.8]
})

df_total = pd.concat([df1, df2], ignore_index=True)
print(df_total)
print()
###########################################################################

# pivot_table() — Resumir dados em tabela dinâmica
# muito usado para agregar dados como em tabelas do Excel.

data = {
    'Categoria': ['Papelaria', 'Papelaria', 'Mochilas', 'Mochilas'],
    'Produto': ['Caneta', 'Lápis', 'Mochila A', 'Mochila B'],
    'Vendas': [100, 150, 200, 180]
}

df = pd.DataFrame(data)

tabela = pd.pivot_table(df, index='Categoria', values='Vendas', aggfunc='sum')
print(tabela)
print()
###########################################################################

# melt() — Deixar os dados em formato longo
# transforma colunas em linhas, útil para dados que precisam de reestruturação.

df3 = pd.DataFrame({
    'Produto': ['Caneta', 'Lápis'],
    'Jan': [10, 15],
    'Fev': [12, 18]
})

meltado = pd.melt(df3, id_vars=['Produto'], var_name='Mês', value_name='Vendas')
print(meltado)
print()

#apply() e map() — Aplicar funções linha a linha

#com apply()
df['Total'] = df.apply(lambda linha: linha['Preço'] * linha['Quantidade'], axis=1)

df['Produto'] = df['Produto'].map(lambda x: x.upper()) # deixa em maiúsculas