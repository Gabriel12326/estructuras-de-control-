"""
Solicita la edad de una persona e imprime si es mayor o menor de edad (mayor de
18 años)
"""
edad=int(input("ingrese su edad:"))
if edad>18:
    print(f"eres mayor de edad.")
elif edad<18:
    print(f"eres menor de edad.")
else:
    print(f"tienes {edad} años de edad.")