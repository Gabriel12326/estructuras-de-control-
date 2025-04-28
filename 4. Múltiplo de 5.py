#Escribe un programa que pida un número y determine si es múltiplo de 5.
numero=int(input("ingresa el numero:"))
if numero % 5 == 0:
   print(f"{numero} es multiplo de 5.")
else:
   print(f"{numero} no es multiplo de 5.")