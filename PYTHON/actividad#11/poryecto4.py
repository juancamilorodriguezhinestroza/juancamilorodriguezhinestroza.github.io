cdfactura=[]
cd_cliente=[]
nombredecliente=[]
faruras=[]
productos=[]
precios=[]
canticades=[]
total=[]



tamaño=int(input("tamaño de la lista?:"))
for i in range(tamaño):

    print("ingrese los datos de facturacion ",i+1)
    print("-----------------------------------------")    
    id_factura=input("id_factura de la factura")
    print("-----------------------------------------")    
    idcliente=input(" cd_cliente del ")
    print("-----------------------------------------")    
    nonbre=input("nombre del cliente ")
    print("-----------------------------------------")    
    factura=input("ingrese  fecha de fafacturacion")
    print("-----------------------------------------")    
    producto=input("productos del aprendiz")
    print("-----------------------------------------")    
    precio=int(input("ingrese el presio del preoducto"))
    print("-----------------------------------------")    
    cantidad=int(input("ingrese la cantidad de productos"))
    print("-----------------------------------------")


    cdfactura.append(id_factura)
    cd_cliente.append(idcliente)
    nombredecliente.append(nonbre)
    faruras.append(factura)
    productos.append(producto)
    precios.append(precio)
    canticades.append(cantidad)
    total.append(cantidad*precio)
    


print("esta es su factura: ")
for i in range(tamaño):
    
    print("-----------------------------------------")
    print("id_factura:" , id_factura[i])
    print("-----------------------------------------")
    print("cd_cliente: ", cd_cliente[i])
    print("-----------------------------------------")
    print("nombredecliente: " , nombredecliente [i])
    print("-----------------------------------------")
    print("faruras: " , faruras [i])
    print("-----------------------------------------")    
    print("productos : " ,productos [i])
    print("-----------------------------------------")    
    print(" precios :" ,precios [i])
    print("-----------------------------------------")    
    print("lugar de precios: " ,canticades [i])
    print("-----------------------------------------")

    print("el total de su facturacion es: " ,total[i])    