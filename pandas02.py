import pandas as pd 

dado = {
    'Produto': ['Caderno', 'Caneta', 'Mochila'],
    'Preço': [12.5, 3.4, 89.9],
    'Quantidade': [10, 50, 5]
}

print(dado.head()) # mostra as primeiras 5 linhas(padrão)

print(dado.tail()) # mostra as últimas 5 linhas

print(dado.info()) # mostra os tipos de dados, colunas, valores nulos, etc

print(dado.describre()) # mostra estatísticas básicas(só colunas númericas)

print(dado['Produto']) # acessa uma coluna (retorna uma Series)

print(dado['Produto', 'Preço']) # acessa várias colunas

print(dado.loc[0]) # acessa pelas labels (índices nomeados) - Linha de índice 0 (primeira linha)

print(dado.iloc[2]) # acessa pela posição (linha N) - Terceira linha

print(dado.iloc[0:2]) # (Fatiando linhas) - Da linha 0 até a 1 (exclui a 2)
###################################################################################################

dado['Total'] = dado['Preço'] * dado['Quantidade'] # adicionar uma nova coluna chamada "Total", que é Preço x Quantidade
print(dado)

dado = dado.drop('Total', axis=1) # Removendo colunas (axis = 1 significa coluna)
print(dado)

dado.rename(columns={'Produto': 'Item', 'Preço': 'Valor'}, inplace=True) #renomeando colunas