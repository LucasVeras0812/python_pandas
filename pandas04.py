import pandas as pd

data = {

}

df = pd.read_csv('nome_do_arquivo.csv') # lendo arquivos CSV

df = pd.read_xlsx('nome_do_arquivo.xlsx') # lendo arquivos EXCEL
# você pode usar o parâmetro sep=';' se o separador não for vírgula.

df.to_csv('saida.csv', index=False) # salvando arquivos CSV

df.to_excel('saida.xlsx', index=False) # salvando arquivos EXCEL

print(df.isnull()) # Mostra True/False onde tem valor nulo
print(df.isnull().num()) # conta quantos valores nulos por coluna

df['coluna'].fillna(0, inplace=True) # preenche valores ausentes com 0
df['coluna'].fillna(df['coluna'].mean(), inplace=True) #Preenche com média

df.dropna(inplace=True) # remover linhas com valores ausentes

df.drop_duplicates(inplace=True) # remover duplicatas

df['Valor'] = df['Valor'].astype(float) # corrigir tipos de dados