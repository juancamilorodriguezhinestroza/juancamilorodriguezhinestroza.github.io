
from turtle import color


marca=[]
modelo=[]
color_b=[]
tipocombustible=[]
silindrage=[]
precios=[]



tamaño=int(input("tamaño de la lista?:"))
for i in range(tamaño):
 print("ingrese los datos del vehiculo",i+1)
 marca_b=input("marca del vehiculo") 
 modelo_b=input("el modedelo del vehiculo")
 color_beiculo=input("ingrese el color de el vehiculo")
 t_combustible=input("ingrese el tipo de combustible")
 silindro=input=("ingrese el silindraje del vehiculo")
 precio=input=("ingrse el precio del vehiculo")


 marca.append(marca_b)
 modelo.append(modelo_b)
 color_b.append(color_beiculo)
 tipocombustible.append(t_combustible)
 silindrage.append(silindro)
 precios.append(precio)



 print("los veiculos son: ")
for i in range(tamaño):
    print("-----------------------------------------")
    print("la marca es : " , marca [i])
    print(" el modelo es: " ,modelo [i])
    print("color:" ,color_b[i])
    print("tipocombustible",tipocombustible [i])
    print("silindrage ", silindrage[i])
    print("el presio de es:" , precio)
