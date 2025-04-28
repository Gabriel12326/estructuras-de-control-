#Pide al usuario tres números y muestra el mayor de ellos
a=int(input("ingrese el primer numero:"))
b=int(input("ingrese el segundo numero:"))
c=int(input("ingrese el tercer numero:"))

if a > b and a > c:
    print(f"{a} es el mayor")
elif b > a and b > c:
    print(f"{b} es el mayor")
elif c > a and c > b:
    print(f"{c} es el mayor")
