# Teoria de Conjuntos

# união
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print ("Conjunto A: ", a)
print ("Conjunto B: ", b)
print ("O conjunto A U B é: ", a.union(b))

#intersecção
print ("O conjunto A ∩ B é: ", a.intersection(b))

#diferença
print ("O conjunto A \ B é: ", a.difference(b))
print ("O conjunto B \ A é: ", b.difference(a))


#diferença simétrica
print ("O conjunto A △ B é: ", a.symmetric_difference(b))