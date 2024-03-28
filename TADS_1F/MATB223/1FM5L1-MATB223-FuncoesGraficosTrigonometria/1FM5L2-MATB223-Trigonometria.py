import matplotlib.pylab as plt
import sympy as sp
import numpy as np

from sympy import (sin, cos, tan, asin, acos, atan, sqrt, symbols, simplify,
                   trigsimp, log, exp, expand, expand_trig, Symbol, rad, deg,
                   sinh, cosh, tanh)

import math


print(math.pi)
# 3.141592653589793

# converte para graus
print(math.degrees(math.pi/2))
# converte para radianos
print(math.radians(90))

# calcula seno de 30 graus
sin30 = math.sin(math.radians(30))
print(sin30)
# 0.49999999999999994

# calcula cosseno de 60 graus
print(math.cos(math.radians(60)))
# 0.5000000000000001

# Calcula qual é o ângulo cujo cosseno é 0,5
print(math.degrees(math.acos(0.5)))
# 59.99999999999999

# podemos trabalhar com frações ou termos de raízes ou PI
a = sin(sp.pi / 6)
print(a)

b = tan(sp.pi / 6)
print(b)

c = rad(30)
print(c)


# imprimir o grafico do seno


x = np.linspace(-np.pi*2, np.pi*2, 201)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()
