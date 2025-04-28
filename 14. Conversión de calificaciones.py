while True:
    try:
        calificacion = int(input("Ingrese la calificación (0-100) o -1 para salir: "))
        msg = ""

        if calificacion == -1:
            msg = "Saliendo del programa..."
            print(msg)
            break
        elif 90 <= calificacion <= 100:
            msg = "Tu calificación es A."
        elif 80 <= calificacion <= 89:
            msg = "Tu calificación es B."
        elif 70 <= calificacion <= 79:
            msg = "Tu calificación es C."
        elif 60 <= calificacion <= 69:
            msg = "Tu calificación es D."
        elif 0 <= calificacion <= 59:
            msg = "Tu calificación es F."
        else:
            msg = "Calificación inválida. Ingresa un número entre 0 y 100."

        print(msg)

    except ValueError:
        print("Error: Ingresa un número válido.")
