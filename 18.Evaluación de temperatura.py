"""
Solicita la temperatura en grados Celsius e imprime un mensaje dependiendo del
valor:
○ Menos de 0°C: “Hace mucho frío”
○ Entre 0°C y 20°C: “Clima fresco”
○ Entre 21°C y 30°C: “Clima agradable”
○ Más de 30°C: “Hace mucho calor”
"""
while True:
    try:
        temperatura = float(input("Ingrese la temperatura en grados Celsius (o escriba 'salir' para terminar): "))

        if temperatura < 0:
            mensaje = "Hace mucho frío ❄️"
        elif 0 <= temperatura <= 20:
            mensaje = "El clima es fresco 🌿"
        elif 21 <= temperatura <= 30:
            mensaje = "El clima es agradable ☀️"
        else:
            mensaje = "Hace mucho calor 🔥"

        print(mensaje)
    
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número o escriba 'salir' para terminar.")
