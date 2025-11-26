def calcular_promedio(Number):
    """
    Calcula el promedio (media aritmética) de una lista de números.
    """
    # Usando la función sum() incorporada para una implementación más Pythonic y clara.
    # Se añade un docstring para explicar qué hace la función.
    
    if not Number:
        # Manejo de casos límite: previene una ZeroDivisionError si la lista está vacía.
        return 0
        
    suma_total = sum(Number)
    cantidad = len(Number)
    
    return suma_total / cantidad

# Ejemplo de uso
datos = [10, 20, 30, 40]
resultado = calcular_promedio(datos)
# print(resultado) # Imprime 25.0