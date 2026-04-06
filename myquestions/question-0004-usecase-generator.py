import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def generar_caso_de_uso_clasificar_prioridad():
    n_samples = 20
    X = np.random.rand(n_samples, 3) * 100
    y = np.random.randint(0, 2, size=n_samples)
    
    # Lógica de salida
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = LogisticRegression()
    model.fit(X_scaled, y)
    
    expected_output = model
    return {'X': X, 'y': y}, expected_output
