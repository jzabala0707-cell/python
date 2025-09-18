# Pedir un número
n = int(input("Ingrese un número: "))

print(f"\n📊 Cuadrados de los números entre 1 y {n}:\n")

for i in range(1, n + 1):
    cuadrado = i ** 2
    if cuadrado % 2 == 0:
        print(f"{i}^2 = {cuadrado} (par)")
    else:
        print(f"{i}^2 = {cuadrado}")