#tuplas
tupla1 = () #tupla vacia
print(tupla1)

tupla2 = ("hola", 11, 4.9, True) #tupla con elementos
print(tupla2)
print(tupla2[1]) #acceder al elemento de la tupla
print(tupla2[2])

tupla3=(0, 1, 2, 3)
tupla4=("A", "B", "C")
tupla5=(tupla3, tupla4)
print(tupla5)
print(tupla5[0])
print(tupla5[1][1])

#operaciones
tupla6 = ("A", "B", "C", "D", "E")
tupla7 = (1, 2, 3, 4, 5)
tupla8 = tupla6 + tupla7 #concatenando
print(tupla8)
print(tupla8[8])

#repetir tupla
tupla9 = (1, 2, 3, 4, 5)
tupla10 = tupla9 * 3
print(tupla10)

#comparar tuplas
tupla11 = ("Rojas",)
tupla12 = (123,)
tupla13 = ("Rosas",)
tupla14 = ("rosas",)
print((tupla11,tupla12) < (tupla13,tupla14))

