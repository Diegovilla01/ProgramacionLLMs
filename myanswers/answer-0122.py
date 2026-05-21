import pandas as pd

def analizar_variacion_precios(df):
    df_sol = df.copy()
    df_sol['fecha'] = pd.to_datetime(df_sol['fecha'])
    df_sol = df_sol.sort_values(['producto_id', 'fecha'])
    df_sol['cambio_precio'] = df_sol.groupby('producto_id')['precio'].diff()
    df_sol['es_subida'] = df_sol['cambio_precio'] > 0
    df_sol = df_sol.dropna(subset=['cambio_precio']).reset_index(drop=True)
    return df_sol
