
#listas  son estrucutras de datos que nos permite almacrnar datoas son iguales que los arrays   son estruturas dinamicas osea puedem mutar
lista1=["Kevin",25,98.3,True,"favio",56.3]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])

print(lista1[0:3])
print(lista1[:2])
print(lista1[3:])

lista1.append("Dante")
print(lista1)

lista1.insert(1,"ecuador")
print(lista1)

lista1.extend(["Kev",110,False])
print(lista1)

print(lista1.index("favio"))
lista1.remove(56.3)
print(lista1)

lista1.pop()

print(lista1)

lista2=["milagro","Naranjo"]
lista3=lista2+lista1
print(lista3)

print(lista2 * 4 )
print("Kevin" in lista1)