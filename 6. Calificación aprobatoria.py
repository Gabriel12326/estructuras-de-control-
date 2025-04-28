"""
Solicita la calificación de un estudiante (0-100) y determina si aprobó (mínimo 60) o
reprobó.
"""
calificacion=int(input("ingrese la calificacion:"))
if calificacion >=60:
    print(f"el estudiante aprobo.")
else:
    print(f"el estudiante rebrobo.") 