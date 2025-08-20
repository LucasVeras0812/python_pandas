import pandas as pd 

dados = [10, 20, 30, 40]
serie = pd.Series(dados)

print(serie)


dados = {
    'Nome': ['Lucas', 'Maria', 'João'],
    'Idade': [21, 10, 23],
    'Cidade': ['Santa Catarina', 'Rio de Janeiro', 'São Paulo']
}

df = pd.DataFrame(dados)
print(df)

#Se tiver um arquivo .csv pode fazer assim para mostrar as 5 primeiras linhas.
# df = pd.read_csv('dados.csv')
# print(df.head())