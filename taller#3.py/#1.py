aprobadas = 0
reprobadas = 0

print("📘 Ingrese 5 notas (de 0 a 5):")

for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    
    if nota >= 3.0:
        print(f"Nota {nota} → Aprobada ✅")
        aprobadas += 1
    else:
        print(f"Nota {nota} → Reprobada ❌")
        reprobadas += 1

print("\n📊 Resumen:")
print(f"Aprobadas: {aprobadas}")
print(f"Reprobadas: {reprobadas}")