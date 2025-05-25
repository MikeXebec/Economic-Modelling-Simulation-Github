# =========================
# GitHub Version - Session 11 (Updated)
# Topic: Midterm Prep – Linear Model Template
# =========================

import numpy as np
from sklearn.linear_model import LinearRegression

def train_linear_model():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([3, 6, 9, 12, 15])

    model = LinearRegression()
    model.fit(X, y)

    print("\n--- Model Coefficients ---")
    print("Intercept:", model.intercept_)
    print("Slope:", model.coef_)

    test_X = np.array([[6], [7]])
    predictions = model.predict(test_X)
    print("Predictions for [6,7]:", predictions)

if __name__ == '__main__':
    train_linear_model()