import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_detectar_fuera_de_limites():
    n_muestras = random.randint(10, 15)
    id_lotes = [f"LOT-{i:03d}" for i in range(n_muestras)]
    medidas = np.round(np.random.normal(50, 0.5, n_muestras), 2)
    
    df = pd.DataFrame({'id_lote': id_lotes, 'medida_mm': medidas})
    lcl, ucl = 49.2, 50.8
    
    # Lógica de salida
    fuera = df[(df['medida_mm'] < lcl) | (df['medida_mm'] > ucl)]['id_lote'].tolist()
    expected_output = {
        'total_lotes': len(df),
        'fuera_de_control': fuera
    }
    
    return {'df_medidas': df, 'lcl': lcl, 'ucl': ucl}, expected_output
