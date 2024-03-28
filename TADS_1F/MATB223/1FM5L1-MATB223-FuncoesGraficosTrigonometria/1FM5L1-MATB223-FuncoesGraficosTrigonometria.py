# instalar o pacote matplotlib
# python3 -m pip install -U matplotlib

import matplotlib.pyplot as plt

# função do primeiro grau => y = ax+b
# Exemplo: y = 2x+1

# Data
x = []
y = []

for val_x in range(-5, 6):
    x.append(val_x)

tam = len(x)
print(x)

i = 0
while i < tam:
    y.append(2*x[i]+1)
    i += 1

print(y)

# Criar uma figura e um eixo
fig, ax = plt.subplots()

# Plotar os dados
ax.plot(x, y)

# Mostrar o gráfico
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y - Função Y = 2x+1')
plt.show()
