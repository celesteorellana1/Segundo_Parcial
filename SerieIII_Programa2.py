import sys

def calcular_suma(valores):
    lista_valores = valores.split(",")
    suma = sum([int(valor) for valor in lista_valores])
    return suma

def calcular_promedio(valores):
    lista_valores = valores.split(",")
    suma = sum([int(valor) for valor in lista_valores])
    promedio = suma / len(lista_valores)
    return promedio

if __name__ == "__main__":
    valores = input("Ingresa los valores separados por comas: ")
    suma = calcular_suma(valores)
    promedio = calcular_promedio(valores)
    print("La suma es", suma)
    print("El promedio es", promedio)