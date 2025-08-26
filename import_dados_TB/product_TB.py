import pandas as pd

oui = pd.read_excel('/Users/lucassv/Desktop/python_pandas/import_dados_TB/tbs_ativos_oui.xlsx')

oui['TB_Datasul'] = oui['TB_Datasul'].astype(str).str.strip().str.upper()
oui['TB_oui'] = oui['TB_oui'].astype(str).str.strip().str.upper()

oui['TB_valido'] = oui['TB_Datasul'].isin(oui['TB_oui'])

oui['TB_nao_encontrado'] = oui.apply(
    lambda row: row['TB_Datasul'] if not row['TB_valido'] else None, axis=1
)

oui.to_excel('conferencia_tbs_final.xlsx', index=False)