numeros = [34, 12, 5, 99, 67, 43, 21]
# Ordenar en orden ascendente
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
print("Orden ascendente:", numeros)

# Ordenar en orden descendente
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] < numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
print("Orden descendente:", numeros)