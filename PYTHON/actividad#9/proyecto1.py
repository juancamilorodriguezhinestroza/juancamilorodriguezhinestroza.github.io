#realise un app que mueste¿re la lista de libros
#con 7 pociciones 
print("nobes de libros")
lista=["la vaca","riqueza de naciones","corazon oscuro","el prinsipito","las estrllas negras","la biblia","el capital"]
lista.append("barracon")
#eliminar elemento de la lista
#primera forma
lista.pop(3)
#segundaforma
lista.remove("python")
for x in lista:
    print(x)

longitud=len(lista)
print("el tamaño o longitud es: " , longitud)

