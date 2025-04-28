"""
Pide al usuario tres números y determina si son todos positivos, todos negativos,
mixtos o si hay ceros.
"""
a=int(input("ingrese el primer numero:"))
b=int(input("ingrese el segundo numero:"))
c=int(input("ingrese el segundo numero:"))

if a > 0 and b > 0 and c >0:
    print(f"todos los numeros son positivos")
elif a < 0 and b < a and c < 0:
    print(f"todos los numeros son negativos")
elif a == 0 or b == 0 or c == 0:
    print(f"tiene ceros")
else:
    print("los numeros son mixtos")
