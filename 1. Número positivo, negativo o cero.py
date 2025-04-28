'''
Escribe un programa que solicite un número al usuario y determine si es positivo,
negativo o cero.
'''
numero=int(input("ingrese un numero:"))

if numero >0:
    print(f"el numero es positivo.")
elif numero <0:
    print(f"el numero es negativo.")
elif numero == 0:
    print(f"el numero tiene 0.")