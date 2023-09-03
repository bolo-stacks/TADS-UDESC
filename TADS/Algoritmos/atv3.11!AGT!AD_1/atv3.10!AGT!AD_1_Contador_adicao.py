"""
Entrada: 
Não há entrada neste algorítmo.

Saída:
I=0 J=1
I=0 J=2
I=0 J=3
I=0,2 J=1,2
I=0,2 J=2,2
I=0,2 J=3,2
.....

I=2 J=3
I=2 J=4
I=2 J=5

.....

"""

i = 0
j_loop = 1

while i <= 2:
    for j_loop in range(1, 4):
        if i == 0 or i == 1:
            print("I=%.0f J=%.0f" % (i, j_loop + i))
        else:
            print("I=%.1f J=%.1f" % (i, j_loop + i))
    i = i + 0.2
