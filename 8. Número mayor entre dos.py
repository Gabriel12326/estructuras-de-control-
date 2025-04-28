"""
Pide al usuario que ingrese dos números y determina cuál es el mayor o si son
iguales
"""
a=int(input("igrese su primer numero:"))
b=int(input("ingrese su segundo numero:"))

if a > b:
    print(f"el numero {a} es mayor que {b}.")
elif b > a:
    print(f"el numero {b} es mayor que {a}.")
else:
    print(f"los numeros {a} y {b} son iguales.")