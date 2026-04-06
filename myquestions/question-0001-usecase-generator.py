import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_analizar_cuello_botella():
    n_estaciones = random.randint(4, 8)
    estaciones = [f"Estacion_{chr(65+i)}" for i in range(n_estaciones)]
    tiempos = np.random.randint(30, 120, size=n_estaciones)
    t_max = 60
    
    df = pd.DataFrame({
        'estacion': estaciones,
        'tiempo_operacion_seg': tiempos
    })
    
    # Lógica de salida
    df_res = df[df['tiempo_operacion_seg'] > t_max].copy()
    df_res['exceso_tiempo'] = df_res['tiempo_operacion_seg'] - t_max
    expected_output = df_res[['estacion', 'exceso_tiempo']].sort_values('exceso_tiempo', ascending=False)
    
    return {'df_tiempos': df, 'tiempo_ciclo_max': t_max}, expected_output
