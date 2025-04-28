"""
Solicita tres números que representan longitudes y determina si pueden formar un
triángulo (la suma de dos lados debe ser mayor que el tercero).
"""
a=float(input("ingrese el primer lado:"))
b=float(input("ingrese el segundo numero:"))
c=float(input("ingrese el tercer numero:"))
if a + b > c and a + c > b and b + c > a:
    print(f"las longitudes pueden formar un triangulo")
else:
    print("no pueden formar un triangulo") 