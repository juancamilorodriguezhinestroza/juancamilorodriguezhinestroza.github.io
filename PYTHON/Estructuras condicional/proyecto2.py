#app que al ingresar el valor de compra#
#si el valor de la compra es mayor a 100.000#
# entond¿ses calcule el descuento (7%)y el total de compra #

valor_compra=float(input("dijite el valor de la compra"))
if valor_compra>100000:

    desduento=valor_compra*0.07
    total =valor_compra-desduento
    print("subtotal:", valor_compra ,)
    print
else:

    desduento=valor_compra*0.07
    total =valor_compra-desduento
    print("subtotal:", valor_compra ,)

