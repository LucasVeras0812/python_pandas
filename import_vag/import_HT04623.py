import pandas as pd

id_nome = pd.read_excel('/Users/lucassv/Desktop/python_pandas/import_vag/nome_v18.xlsx')
planilha_final = pd.read_excel('/Users/lucassv/Desktop/python_pandas/import_vag/planilha_final_v18.xlsx')

merge = pd.merge(id_nome, planilha_final, on='ID Externo', how='left')

res = merge[['ID Externo', 'Nome', 'Suporte de Venda', 'Product Manager']]

res.to_excel('planilha_completa.xlsx', index=False)