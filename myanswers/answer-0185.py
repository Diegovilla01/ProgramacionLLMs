import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

def optimizar_modelo_logistica(X, y):
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("rf", RandomForestRegressor(random_state=42))
    ])

    param_grid = {
        "rf__n_estimators": [50, 100],
        "rf__max_depth": [None, 5, 10]
    }

    grid = GridSearchCV(
        pipeline,
        param_grid,
        cv=3,
        scoring="neg_mean_absolute_error"
    )

    grid.fit(X, y)

    return {
        "mejor_modelo": grid.best_estimator_,
        "mejor_mae": abs(grid.best_score_)
    }
