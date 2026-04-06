import numpy as np
from sklearn.linear_model import LinearRegression

def generar_caso_de_uso_predecir_consumo_energia():
    X = np.array([[100], [200], [300], [400], [500]])
    y = np.array([150, 290, 460, 610, 740]) # Relación casi lineal
    X_new = np.array([[250], [450]])
    
    # Lógica de salida
    model = LinearRegression()
    model.fit(X, y)
    expected_output = model.predict(X_new)
    
    return {'X': X, 'y': y, 'X_new': X_new}, expected_output
