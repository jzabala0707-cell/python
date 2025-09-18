# Pedir palabra y letra
palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra: ")

# Contador
contador = 0

for caracter in palabra:
    if caracter == letra:
        contador += 1

# Mostrar resultado
if contador > 0:
    print(f"La letra '{letra}' aparece {contador} vez/veces en la palabra '{palabra}'.")
else:
    print(f"La letra '{letra}' no aparece en la palabra '{palabra}'.")