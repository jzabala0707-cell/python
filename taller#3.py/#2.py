positivos = 0
negativos = 0
ceros = 0

print("🔢 Ingrese 5 números enteros:")

for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1

print("\n📊 Resultados:")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")