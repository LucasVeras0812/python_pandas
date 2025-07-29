import pandas as pd
import os

# ler os dois arquivos
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'contatos_v13_completos.xlsx')
v13 = pd.read_excel(file_path)

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'contatos_v18_parciais.xlsx')
v18 = pd.read_excel(file_path)

# limpar espaços e padronizar nomes de colunas
v13.columns = v13.columns.str.strip()
v18.columns = v18.columns.str.strip()

# renomear para garantir correspondência na chave de junção
v18.rename(columns={'ID externo': 'ID Externo'}, inplace=True)

# fazer o merge
dados_completos = pd.merge(v18, v13, on='ID Externo', how='left', suffixes=('_v18','_v13'))

# selecionar os campos desejados
campos_para_atualizar = dados_completos[[
    'ID Externo',
    'Nome_v13',
    'CNPJ/CPF',
    'CEP',
    'Endereço',
    'Cidade',
    'Estado',
    'País',
    'E-mail',
    'Telefone',
    'Celular',
    'Link do Site'
]]

# exportar resultado
campos_para_atualizar.to_excel('contatos_v18_atualizados.xlsx', index=False)

print('Nova planilha gerada com sucesso!')