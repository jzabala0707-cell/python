numeros = (15, 28, 2, 70, 7, 42)
maximo = numeros[0]
minimo = numeros[0]
for num in numeros:
    if num > maximo:
        maximo = num
    if num < minimo:
        minimo = num
print("Máximo:", maximo)
print("Mínimo:", minimo)