"""
Pide al usuario su salario mensual y aplica los siguientes impuestos:
○ Menos de 10,000: 0%
○ Entre 10,000 y 30,000: 10%
○ Más de 30,000: 20%
"""
salario=float(input("ingrese su salario mensual:"))

if salario < 10000:
 print(f"tienes un impuesto a pagar de 0%.")
elif salario >=10000 and salario <=30000:
    print(f"tienes un impuesto a pagar de 10%.")
else:
    print(f"tienes un impuesto a pagar de 20%.")