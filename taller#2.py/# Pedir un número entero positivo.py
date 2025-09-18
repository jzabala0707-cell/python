# Pedir un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

# Inicializar suma
suma_pares = 0

# Recorrer desde 1 hasta n
for i in range(1, n + 1):
    if i % 2 == 0:  # Verificar si es par
        suma_pares += i

# Mostrar resultado
print(f"La suma de los números pares entre 1 y {n} es: {suma_pares}")