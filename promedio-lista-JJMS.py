def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    lista_numeros (list): Lista de números (int o float)

    Retorna:
    float: Promedio de los números en la lista
    """
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

# Ejemplo de uso:
numeros = [10, 20, 30, 40]
print("Promedio:", calcular_promedio(numeros))
