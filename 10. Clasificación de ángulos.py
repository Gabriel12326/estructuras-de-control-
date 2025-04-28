"""
Solicita al usuario el valor de un ángulo en grados y determina si es agudo (<90°),
recto (90°), obtuso (>90° y <180°) o llano (180°).
"""
valor=float(input("ingrese el valor del angulo en grados:"))
if valor<90:
    print(f"el angulo es agudo.")
elif valor == 90:
    print(f"el angulo es recto.")
elif valor >90 and valor <180:
    print(f"el angulo es obtuso.")
elif valor == 180:
    print(f"el angulo es llano.")

else:
    print("el angulo no es valido, (debe de ser entre 0 a 180 grados.")
