from spatialmath.base import rot2
from sympy import simplify, Matrix
import spatialmath.base as base
import numpy as np

R = rot2(0.2)
det = np.linalg.det(R)
print("La matriz es \n", R)
print("Su determinante es", det)
det_RxR = np.linalg.det(np.matmul(R, R))
print("El determinante de R*R es", det_RxR)