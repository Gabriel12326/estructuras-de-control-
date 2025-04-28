"""
Escribe un programa que solicite un número del 1 al 7 y muestre el día de la
semana correspondiente (1 es lunes, 7 es domingo).
"""
numero=int(input("ingrese un numero del 1 al 7:"))

if numero == 1:
  print(f"es lunes")
elif numero == 2:
  print(f"es martes")
elif numero == 3:
  print(f"es miercoles")
elif numero == 4:
  print(f"es jueves")
elif numero == 5:
  print(f"es viernes")
elif numero == 6:
  print(f"es sabado")
elif numero ==7:
  print(f"es domingo")
else:
  print("numero no valido, debes imgresar un numero del 1 al 7")