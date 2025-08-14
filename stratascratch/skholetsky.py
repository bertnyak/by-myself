from scipy.linalg import lu
import numpy as np
A = np.array([[0, 91, 26],
              [60, 3, 75],
              [45, 90, 31]], dtype='float')
_, L, U = lu(A)
print(L)
print(U)