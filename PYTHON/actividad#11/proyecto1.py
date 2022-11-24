nombres=[]
identificacion=[]
correo=[]
telefono=[]
direccion=[]
nacimiento=[]
lugar_nacimiemto=[]



tamaño=int(input("tamaño de la lista?:"))
for i in range(tamaño):
    print("ingrese los datos del aprendiz",i+1)
    print("-----------------------------------------")    
    nombre=input("nombre del aprendiz")
    print("-----------------------------------------")    
    id=input("N° de identificacion del aprendiz")
    print("-----------------------------------------")    
    gmail=input("correo del aprendiz")
    print("-----------------------------------------")    
    numero=input("N° de telefono del aprndiz")
    print("-----------------------------------------")    
    idc=input("direccion del aprendiz")
    print("-----------------------------------------")    
    f_nacimiento=input("fecha de naciumiento del apremdiz")
    print("-----------------------------------------")    
    l_nacimiento=input("lugar de nacimiento del aprendiz")
    print("-----------------------------------------")
    nombres.append(nombre)
    identificacion.append(id)
    correo.append(gmail)
    telefono.append(numero)
    direccion.append(idc)
    nacimiento.append(f_nacimiento)
    lugar_nacimiemto.append(l_nacimiento)

print("los aprendices son: ")
for i in range(tamaño):
    print("-----------------------------------------")
    print("nombre:" , nombre[i])
    print("-----------------------------------------")
    print("identificacion: ", identificacion[i])
    print("-----------------------------------------")
    print("correo: " , correo [i])
    print("-----------------------------------------")
    print("telefono: " , telefono [i])
    print("-----------------------------------------")    
    print("direccion : " ,direccion)
    print("-----------------------------------------")    
    print("fecha de nacimiento :" ,nacimiento)
    print("-----------------------------------------")    
    print("lugar de nacimiento: " ,lugar_nacimiemto)
    print("-----------------------------------------")    