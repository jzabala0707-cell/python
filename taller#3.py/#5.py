# Pedir límite
limite = int(input("Ingrese un número límite: "))

print(f"\n🔢 Números primos entre 1 y {limite}:\n")

for num in range(2, limite + 1):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)