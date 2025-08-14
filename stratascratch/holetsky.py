import numpy as np

def lu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    for i in range(n - 1):
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
    return L, U

A = np.array([[60, 91, 26],
              [60, 3, 75],
              [45, 90, 31]], dtype='float')

L, U = lu(A)  # Получаем L и U
check = np.allclose(A, L @ U)  # Проверяем корректность разложения

print("L:\n", L)
print("U:\n", U)
print("Проверка A == L@U:", check)