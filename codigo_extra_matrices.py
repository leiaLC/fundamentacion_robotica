import numpy as np
from sympy import symbols, cos, sin, sqrt, simplify

# Definir variables simbólicas
theta1, theta2, theta3, theta4, theta5, theta6 = symbols('theta1 theta2 theta3 theta4 theta5 theta6')

# Definir las matrices A y B
#A es la matríz resultante de (T de 0 a 1) * (T de 1 a 2)
A = np.array([
    [[-sqrt(2)*sin(theta1)*sin(theta2)/2 + cos(theta1)*cos(theta2), -sin(theta1)*cos(theta2)/2 - sin(theta1)/2 - sqrt(2)*sin(theta2)*cos(theta1)/2, -sin(theta1)*cos(theta2)/2 + sin(theta1)/2 - sqrt(2)*sin(theta2)*cos(theta1)/2, 425*sqrt(2)*sin(theta1)*sin(theta2)/2 - 425*cos(theta1)*cos(theta2)], [sin(theta1)*cos(theta2) + sqrt(2)*sin(theta2)*cos(theta1)/2, -sqrt(2)*sin(theta1)*sin(theta2)/2 + cos(theta1)*cos(theta2)/2 + cos(theta1)/2, -sqrt(2)*sin(theta1)*sin(theta2)/2 + cos(theta1)*cos(theta2)/2 - cos(theta1)/2, -425*sin(theta1)*cos(theta2) - 425*sqrt(2)*sin(theta2)*cos(theta1)/2], [sqrt(2)*sin(theta2)/2, cos(theta2)/2 - 1/2, cos(theta2)/2 + 1/2, -425*sqrt(2)*sin(theta2)/2 + 89], [0, 0, 0, 1]]
])

#T de 2 a 3
B = np.array([
    [cos(theta3), -sqrt(2)/2*sin(theta3), sqrt(2)/2*sin(theta3), -392*cos(theta3)],
    [sin(theta3), sqrt(2)/2*cos(theta3), -sqrt(2)/2*cos(theta3), -392*sin(theta3)],
    [0, sqrt(2)/2, sqrt(2)/2, 0],
    [0, 0, 0, 1]
])

#T de 3 a 4
C = np.array([
    [cos(theta4), -sqrt(2)/2*sin(theta4), -sqrt(2)/2*sin(theta4), 0],
    [sin(theta4), sqrt(2)/2*cos(theta4), sqrt(2)/2*cos(theta4), 0],
    [0, -sqrt(2)/2, sqrt(2)/2, 109],
    [0, 0, 0, 1]
])

#T de 4 a 5
D = np.array([
    [cos(theta5), sqrt(2)/2*sin(theta5), sqrt(2)/2*sin(theta5), 0],
    [sin(theta5), -sqrt(2)/2*cos(theta5), -sqrt(2)/2*cos(theta5), 0],
    [0, sqrt(2)/2, sqrt(2)/2, 94],
    [0, 0, 0, 1]
])

#T de 5 a 6
E = np.array([
    [cos(theta6), -sqrt(2)/2*sin(theta6), -sqrt(2)/2*sin(theta6), 0],
    [sin(theta6), sqrt(2)/2*cos(theta6), sqrt(2)/2*cos(theta6), 0],
    [0, -sqrt(2)/2, sqrt(2)/2, 82],
    [0, 0, 0, 1]
])

#T de 0 a 3
# Multiplicar las matrices
F = np.dot(A, B)

# Simplificar el resultado
F_simplified = simplify(F)

print(F_simplified)

#T de 0 a 4
G = np.dot(F, C)

# Simplificar el resultado
G_simplified = simplify(G)

print(G_simplified)

#T de 0 a 5
H = np.dot(G, D)

# Simplificar el resultado
H_simplified = simplify(H)

print(H_simplified)

#T de 0 a 6
I = np.dot(H, E)

# Simplificar el resultado
I_simplified = simplify(I)

print(I_simplified)


