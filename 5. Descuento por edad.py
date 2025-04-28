"""
Un cine ofrece un descuento del 50% a personas mayores de 60 años. Solicita la
edad del usuario y determina si aplica para el descuento.
"""
edad=int(input("solicite su edad:"))
if edad >60:
    print(f"¡felicidades! usted tiene un descuento de 50%.")
else:
    print(f"lo sentimos, usted no aplica para el descuento.")