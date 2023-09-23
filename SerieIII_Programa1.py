def contar_letra(string, letra):
    contador = 0
    for caracter in string:
        if caracter.lower() == letra.lower():
            contador += 1
    return contador

# Ejemplo de uso:
texto = input("Ingresa un texto: ")
letra_buscar = input("Ingresa una letra: ")
resultado = contar_letra(texto, letra_buscar)
print("La letra", letra_buscar, "aparece", resultado, "veces en el texto."),