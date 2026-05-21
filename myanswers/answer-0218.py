import pandas as pd

def procesar_info_contacto(df):
    df_result = df.copy()
    df_result[['nombre', 'telefono', 'departamento']] = df_result['info_contacto'].str.split('-', expand=True)
    df_result = df_result.drop(columns=['info_contacto'])
    df_result = df_result[df_result['departamento'].isin(['Ventas', 'IT'])]
    return df_result
