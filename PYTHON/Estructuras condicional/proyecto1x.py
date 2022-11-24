"""Evaluar la edad ingresada
0>= y <2, Eres un baby
2>=y <12, Eres un niño(a)
12>=y <=17, Eres un Adolecente
18>=y <40, Eres un Adulto Joven
40>=y <60, Eres un Adulto Maduro
>=60, Eres un Adulto Mayor
"""
edad=int(input("Ingrese la Edad"))
if edad >=0 and edad<2:
    print("Eres un Baby")
elif edad >=2 and edad<12:
    print("Eres un niño(a)")
elif edad >=12 and edad<=17:
    print("Eres un Adolecente")
elif edad >=18 and edad<40:
    print("Eres un Adulto Joven")