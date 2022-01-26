from sympy import *

x = Symbol("x")
fx = -x**4-2*x**3-8*x**2-5*x
fxp = fx.diff(x)
fxpp = fxp.diff(x)

x0 = -1
error = 1
tolerancia = 0.0001
iteracion = 1

print("X0: ", x0, " |Tolerancia: ", tolerancia)

#print("Desc funcion: ", fx,"| Desc f prima: ", fxp, "| Desc f doble prima: ", fxpp)

while error > tolerancia:
    valfx = fx.subs(x, x0)
    valfxp = fxp.subs(x, x0)
    valfxpp = fxpp.subs(x, x0)

    #print("X0: ", x0, " |Eval funcion: ", valfx, "| Eval f prima: ", valfxp, "| Eval f doble prima: ", valfxpp)

    x1 = x0 - (valfxp/valfxpp)
    error = abs(x1 - x0)
    print("Iteración: ", iteracion, " |X1: ", x1+0.01-0.01 , " |fx1: ", fx.subs(x, x1)+0.01-0.01, " |Error: ", error+0.01-0.01)
    x0 = x1
    iteracion = iteracion + 1





