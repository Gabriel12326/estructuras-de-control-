#Pide al usuario que ingrese un número entero y determina si es par o impar.
numero=int(input("Digite un numero:"))

if numero % 2 ==0:
    print(f"el numero {numero} es par.")
else:
    print(f"el numero {numero} es impar.")