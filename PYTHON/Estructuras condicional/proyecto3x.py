imc=float(input("digite el peso en kg: "))
imc=float(input("digite la estatura en metros: "))
if imc < 18.5:
    print("BAJO PESO")
elif imc >=18.5 and imc <=24.9:
    print("PESO NORMAL")
elif imc >=25 and imc <=29.9:
    print("SOBREPESO")
elif imc >=30 and imc <=34.9:
    print("OBECIDAD I")
elif imc >=35 and imc <=39.9:
    print("OBECIDAD II")
elif imc >=40 and imc <=49.9:
    print("OBECIDAD III")
elif imc >=50:
    print("OBECIDAD IV")
else:
    print("Escriba los valores numericos esperados...")