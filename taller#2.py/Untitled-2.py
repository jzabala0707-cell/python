while True:
    print("\n📌 Menú de Operaciones Matemáticas")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elija una opción (1-10): ")

    if opcion == "10":
        print("👋 Gracias por usar el programa. ¡Adiós!")
        break

    # Pedir números solo si no eligió salir
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == "1":
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif opcion == "2":
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif opcion == "3":
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif opcion == "4":
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("⚠️ Error: No se puede dividir entre 0.")
    else:
        print("❌ Opción no válida, intente de nuevo.")