

def calcular_calificacion_final(cal1, cal2, cal3, examen, trabajo):
    """
    Calcula la calificación final de un estudiante a partir de:
    - Tres calificaciones parciales
    - Nota del examen
    - Nota del trabajo final

    Fórmula aplicada:
        promedio = ((cal1 + cal2 + cal3) / 3) * 0.55
        calificación final = promedio + (examen * 0.30) + (trabajo * 0.15)

    Parámetros:
        cal1 (float): Primera calificación parcial.
        cal2 (float): Segunda calificación parcial.
        cal3 (float): Tercera calificación parcial.
        examen (float): Nota del examen final.
        trabajo (float): Nota del trabajo final.

    Retorna:
        float: La calificación final calculada.
    """

    # Calcular el promedio ponderado de las tres notas parciales
    promedio = ((cal1, cal2, cal3)) / 3 * 0.55

    # Calcular la nota final combinando examen y trabajo
    calificacion_final = promedio + (examen * 0.30) + (trabajo * 0.15)

    return calificacion_final


# --------- Prueba de la función ---------
if __name__ == "__main__":
    print("=== Cálculo de Calificación Final ===")

    # Solicitar datos al usuario
    cal1 = float(input("Dame la primera calificación: "))
    cal2 = float(input("Dame la segunda calificación: "))
    cal3 = float(input("Dame la tercera calificación: "))
    examen = float(input("Dame la nota del examen: "))
    trabajo = float(input("Dame la nota del trabajo: "))

    # Usar la función
    resultado = calcular_calificacion_final(cal1, cal2, cal3, examen, trabajo)

    # Mostrar resultado
    print(f"\nTu calificación final es: {resultado}")
