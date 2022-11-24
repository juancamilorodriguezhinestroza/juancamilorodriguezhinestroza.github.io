nombre=input("ingrese su nombre")
edad=input("ingrese su edad")
direccion=input("ingrese su direccion")
telefono=input("ingrese su numero de telefono")


persona={"nombre":nombre,"edad":edad,"direccion":direccion,"telefono":telefono}
print(persona["nombre"],"tiene :",
persona["edad"],"años",", y vive ",
persona["direccion"],"y su numero de telefono es ", 
persona["telefono"],
)


# que permita a el usuario ingrezar fruta y el precio unitario y la cantida y lo amasene em un diccionario llamado factura
#despues debe mostrar un mensaje concatenado donde aparese el nombre de la fruta du valor la cantidad y el total
fruta=input("ingrese su nombre de la fruta")
cantidades=input("ingrese la cantidad a lleyar")
unitario=int( input("ingrese el predio unitario"))
factuta={"fruta":fruta,"cantidades":cantidades,"unitario":unitario }
 
factuta={"fruta":fruta , "unitario":unitario}
print(factuta["fruta"],"tiene un valor unitario de :",
factuta["unitario"],"y su total de compra es de",
(cantidades*unitario ) 
)


#diseñe una app que permita almacenar ña informacion de los clientes de una empresa
#los clieentes se guardaran en un diccionario llamado clientes 
#los datos deben ser ingresados por el usuario
#identificacion de cliente 
#nombre direccion telefono correo empresa
#la apple debe preguntar por una opcion del menu
#mostrar cliente
#eliminar clientes
#salir o finalizar
cliente={}
op=""
while op !=4:
      
 if op ==1:
      identificacion=input("ingrese su identificacion")
      nombre=input("ingrese su nombe")
      direccion=input("ingrese su direccipon")
      telefono=input("ingrese su telefono")
      correo=input("ingrese su correo")
      empresa=input("ingese el nombre de la empresa")
      cliente={"identificacion":identificacion,
      "nombre":nombre,
      "direccion":direccion,
      "telefono": telefono ,
      "empresa":empresa
  

   }

if op == 2:
       print("informacion del cliente")
       print("identificacion",cliente["Aidentificacion"])
       print("nombre",cliente["nombre"])
       print("direccion",cliente["direccion"])
       print("telefono",cliente["telefono"])
       print("correo",cliente["correo"])
       print("empresa",cliente["empresa"])
if op == 3:
       del[identificacion]
       print("cliente eliminado con exito")
if op == 4:
    
    exit()
print("---menu---")
print("1-AÑADIR CLIENTE")
print("2-MOSTRARCLIENTE")
print("3-ELIMINAR CLIENTE")
print("4-SALIR")  
input("escoja una occipon de este menu")