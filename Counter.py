from collections import Counter

# Texto quemado en el código
texto = "Este es un ejemplo de texto con palabras repetidas este texto es solo un ejemplo"

# Convertir el texto a minúsculas y dividirlo en palabras
palabras = texto.lower().split()

# Contar la frecuencia de cada palabra
frecuencia_palabras = Counter(palabras)

# Mostrar el resultado
print("Frecuencia de palabras repetidas:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")
