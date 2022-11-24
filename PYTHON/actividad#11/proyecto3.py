titulos=[]
generos=[]
duracion=[]
proragonista=[]
estrenos=[]
precios=[]
idiomas=[]



tamaño=int(input("tamaño de la lista?:"))
for i in range(tamaño):
    print("ingrese los datos de la app",i+1)
    print("-----------------------------------------")    
    titulo=input("ingrese el titulo de la pelicula ")
    print("-----------------------------------------")    
    genero=input("ingrese el gnero de la pelicula")
    print("-----------------------------------------")    
    tiempo=input("ingrese el tiempo que dura la pelicula")
    print("-----------------------------------------")    
    prota=input("ingrese el titulo de el proragonista de la pelicula")
    print("-----------------------------------------")    
    estreno=input("estrenos de la pelicula")
    print("-----------------------------------------")    
    precio=input("ingrese el prcio de lapelicula")
    print("-----------------------------------------")    
    idioma=input("lugar de precios del aprendiz")
    print("-----------------------------------------")
    titulos.append(titulo)
    generos.append(genero)
    duracion.append(tiempo)
    proragonista.append(prota)
    estrenos.append(estreno)
    precios.append(precio)
    idiomas.append(idioma)

print(" Las pelis  son: ")
for i in range(tamaño):
    print("-----------------------------------------")
    print("titulo:" , titulo[i])
    print("-----------------------------------------")
    print("identificacion: ", genero[i])
    print("-----------------------------------------")
    print("correo: " , duracion [i])
    print("-----------------------------------------")
    print("proragonista: " , proragonista [i])
    print("-----------------------------------------")    
    print("estrenos : " ,estrenos [i])
    print("-----------------------------------------")    
    print("fecha de precios :" ,precios [i])
    print("-----------------------------------------")    
    print("idioma : " ,idiomas [i])
    print("-----------------------------------------")    