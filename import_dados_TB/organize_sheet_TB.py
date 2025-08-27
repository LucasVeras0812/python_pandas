import pandas as pd

oui = pd.read_excel('/Users/lucassv/Desktop/python_pandas/import_dados_TB/conferencia_tbs_final.xlsx')

oui['TB_Datasul'] = oui['TB_Datasul'].astype(str).str.strip().str.upper()
oui['TB_oui'] = oui['TB_oui'].astype(str).str.strip().str.upper()

def organizar_linha(row, oui_tbs_ativos):
    if row['TB_Datasul'] in oui_tbs_ativos:
        return pd.Series({
            'TB_oui': row['TB_Datasul'],
            'TB_valido': row['TB_Datasul'],
            'TB_nao_encontrado': 'TB Encontrado'
        })
    else:
        return pd.Series({
            'TB_oui': 'TB Não encontrado',
            'TB_valido': 'TB Não encontrado',
            'TB_nao_encontrado': row['TB_Datasul']
        })

oui_tbs_ativos = oui['TB_oui'].tolist()

resultado = oui.copy()
resultado[['TB_oui', 'TB_valido', 'TB_nao_encontrado']] = resultado.apply(
    organizar_linha, axis=1, oui_tbs_ativos=oui_tbs_ativos
)

resultado.to_excel('conferencia_tbs_organizada.xlsx', index=False)