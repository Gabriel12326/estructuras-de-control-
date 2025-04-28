"""
Pide la hora (0-23) y determina si es "Mañana" (6-11), "Tarde" (12-17), "Noche"
(18-23) o "Madrugada" (0-5).
"""
hora=int(input("ingrese la hora en formato de 0-23:"))
if 0<= hora <=5:
    print(f"son la {hora} de la madrugada.")
elif 6<= hora <=11:
    print(f"son la {hora} de la mañana.")
elif 12<= hora <=17:
    print(f"son la {hora} de la tarde.")
elif 18<= hora <=23:
    print(f"son la {hora} de la noche")
else:
    print("lo sentimos, su hora esta afuera del rango especificado.")
