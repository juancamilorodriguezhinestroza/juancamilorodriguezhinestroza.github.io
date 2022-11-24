#app que muestre los colores
print("lista de colores ")
lista=["blanco","negro","azul","verde","amarillo","rojo","morado"]
lista.append("azul marino")
#eliminar elemento de la lista
#primera forma
lista.pop(3)
#segundaforma
lista.remove("python")
for x in lista:
    print(x)
longitud=len(lista)
print("el tamaño o longitud es: " , longitud)
