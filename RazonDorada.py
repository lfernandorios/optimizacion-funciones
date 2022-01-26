fx = lambda x: -2.5*pow(x, 5) - 2*pow(x, 4) + 12*x

val_xl = 0
val_xu = 2
val_tolerancia = 0.0005

print("X lower: ", val_xl, " | X upper: ", val_xu, " | Tolerancia: ", val_tolerancia)

def seccionDorada(fx, xl, xu, tolerancia):
  error = 1
  iteracion = 0

  while(error > tolerancia):

    d = 0.618 * (xu - xl)
    x1 = xl + d
    x2 = xu - d

    error = abs(x2 - x1)
    print("Iteración: ", iteracion , " | xl: ", xl, ", | xu: ", xu, ", | error: ", error)
    iteracion = iteracion + 1

    if(fx(x2) > fx(x1)):
      xl = xl
      xu = x1
    else:
      xu = xu
      xl = x2

seccionDorada(fx, val_xl, val_xu, val_tolerancia)
