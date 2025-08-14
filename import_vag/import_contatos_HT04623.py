import pandas as pd

v13 = pd.read_excel('/Users/lucassv/Desktop/python_pandas/import_vag/contatos_v13.xlsx')
v18 = pd.read_excel('/Users/lucassv/Desktop/python_pandas/import_vag/contatos_v18.xlsx')

v18.rename(columns={'ID externo': 'ID Externo'}, inplace=True)

valores_validos_atendimento = [
    'Giovana Silveira e Silva',
    'Gabriela Hoffmann Diel',
    'Jessica Alves Silva'
]

valores_validos_gerente = [
    'Rhuamm Ivo Stumf Werner',
    'Zulmar de Lins Neves Neto',
    'Lizandra Ramos Mussio',
    'Bruna dos Santos Rosa'
]

v13['Resp. Atendimento'] = v13['Resp. Atendimento'].where(v13['Resp. Atendimento'].isin(valores_validos_atendimento), '')
v13['Gerente de Produtos'] = v13['Gerente de Produtos'].where(v13['Gerente de Produtos'].isin(valores_validos_gerente), '')

planilha_final = pd.merge(v18, v13, on='ID Externo', how='left', suffixes=('', '_v13'))

planilha_final['Suporte de Venda'] = planilha_final['Resp. Atendimento']
planilha_final['Product Manager'] = planilha_final['Gerente de Produtos']

planilha_final.drop(columns=['Resp. Atendimento', 'Gerente de Produtos'], inplace=True)

planilha_final.to_excel('planilha_final_v18.xlsx', index=False)