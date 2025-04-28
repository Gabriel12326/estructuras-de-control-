#Pide tres longitudes y determina si el triángulo es equilátero, isósceles o escaleno
a=float(input("ingrese la primera longitud:"))
b=float(input("ingrese la segunda longitud:"))
c=float(input("ingrese la tercera longitud:"))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print(f"el triangulo es equilatero")
    elif a == b or a == b or a == c:
        print(f"el triangulo es isosceles.")
    else:
        print("el triangulo es escaleno.")
else:
    print("la lingitudes no pueden formar el triangulo.")