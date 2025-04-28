"""
Solicita el precio de un producto y aplica descuentos según el monto:
○ Menos de $50: sin descuento
○ Entre $50 y $100: 5%
○ Más de $100: 10%
"""
precio=float(input("ingrese el precio del producto:"))

if precio < 50:
    print(f"este producto no tiene descuento.")
elif precio >=50 and precio <= 100:
    print(f"este producto tiene un descuento de 5%.")
else:
    print("este producto tiene un descuento de 10%.")