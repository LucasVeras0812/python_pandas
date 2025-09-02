import pandas as pd 

nome = [
    'Lucas',
    'Estefany'
]

df = pd.read_excel('/Users/lucassv/Desktop/python_pandas/import_dados_TB/teste.xlsx')

df_filtrado = df[df['Nome'].isin(nome)]

colunas_manter = [
    'Nome',
    'Idade',
    'Gênero',
]

df_final = df_filtrado[colunas_manter]

df_final.to_excel('planilha_test.xlsx', index=False)