import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def detect_outliers(df, threshold=3):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)
    result = pd.DataFrame(np.abs(scaled) > threshold, columns=df.columns, index=df.index)
    return result
