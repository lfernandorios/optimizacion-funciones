from pprint import pprint
from math import sin


def fx(x, F):
    rx = 0

    for i, p in enumerate(F):
        rx = rx + (p[0]*x**p[1])
    return rx


def xn(xi, funcion):
    rx = (fx(xi[0], funcion)*(xi[1]**2 - xi[2]**2)+\
         fx(xi[1], funcion)*(xi[2]**2 - xi[0]**2)+\
         fx(xi[2], funcion)*(xi[0]**2 - xi[1]**2))/ \
         (2*fx(xi[0], funcion) * (xi[1] - xi[2]) + \
          2*fx(xi[1], funcion) * (xi[2] - xi[0]) + \
          2*fx(xi[2], funcion) * (xi[0] - xi[1]))
    return rx


#funcion = [(-1, 2), (8, 1), (-12, 0)]
funcion = [(-1, 4), (-2, 3), (-8, 2), (-5, 1)]
#funcion = [(2, 1), (-1/10, 2)]
#Xi = [0, 2, 6]
Xi = [-2, -1, 1]
error = 1
tolerancia = 0.0001
iteracion = 1

print("Puntos: ", Xi, " |Tolerancia: ", tolerancia)

while error > tolerancia:

    x3 = xn(Xi, funcion)
    f3 = fx(x3, funcion)
    f1 = fx(Xi[1], funcion)
    error = abs(Xi[2] - x3)
    print("Iteración: ", iteracion, " |X3:", x3, " |f(X3): ", f3, " |Error: " ,error)
    print("Puntos: ", Xi)

    if (x3 > Xi[1]):
        Xi[0] = Xi[1]
        Xi[1] = x3

    elif (x3 < Xi[1]):
        Xi[2] = Xi[1]
        Xi[1] = x3

    elif (x3 == Xi[1]):
        break

    iteracion = iteracion + 1


