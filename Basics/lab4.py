# Generador de patrones numericos
# Nombre: Josue
# Fecha: 6-Marzo-2026

def number_pattern(n):
    numeros_como_texto = []
    if not isinstance(n, int):
        return "Argument must be an integer value"
    if n < 1:
        return "Argument must be an integer greater than 0"
        
    for i in range (1, n+1):
        numeros_como_texto.append(str(i))
        
    resultado = " ".join(numeros_como_texto)
    return resultado
print(number_pattern(0))
    