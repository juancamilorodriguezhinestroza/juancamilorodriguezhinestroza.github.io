#realise una lista que mustre las plantas medicinales 
print("lista de las plantas medicinales")

lista=[" Cola de caballo","aloe vera","mansanilla","hierbabuena","la moringa",]
lista.append("Orégano")
#eliminar elemento de la lista
#primera forma
lista.pop(3)
#segundaforma
lista.remove("python")
for x in lista:
    print(x)

longitud=len(lista)
print("el tamaño o longitud es: " , longitud)
