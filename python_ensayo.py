# ====== VERSIÓN CON 20 ERRORES INTENCIONALES ======

# Diccionario con productos, stock y descuento del 10%
productos = {
    "arroz": {"precio_unit": 2100, "stock": 10, "descuento": 0.10},
    "fideos": {"precio_unit": 1800, "stock": 15, "descuento": 0.10},     # ERROR 4
    "leche": {"precio_unit": 4200, "stock": 5, "descuento": 0.10},
    "pan": {"precio_unit": 2000, "stock": 20, "descuento": 0.10},
    "huevos": {"precio_unit": 600, "stock": 30, "descuento": 0.10},          # ERROR 3
    "azucar": {"precio_unit": 2800, "stock": 15, "descuento": 0.10},        # ERROR 2
    "cafe": {"precio_unit": 12500, "stock": 8, "descuento": 0.10},
    "aceite": {"precio_unit": 9800, "stock": 6, "descuento": 0.10},
    "panela": {"precio_unit": 4000, "stock": 12, "descuento": 0.10},
    "sal": {"precio_unit": 1500, "stock": 18, "descuento": 0.10},
    "mantequilla": {"precio_unit": 5000, "stock": 7, "descuento": 0.10},
    "arepas": {"precio_unit": 2000, "stock": 25, "descuento": 0.10},
}

IVA_TASA = 0.19   # ERROR 1 

# Lista para guardar compras
carrito = []       # ERROR 5

print("🛒 Bienvenido a la Tienda de Víveres 🛒\n")
print("Productos disponibles:")
# ERROR 6: .item() en vez de .items()
for producto, datos in productos.items():
    # ERROR 7
    # ERROR 8
    print(f"- {producto.capitalize()} | Precio: {datos.get('precio_unit', 'N/A')} | Stock: {datos['stock']} | Descuento: {int(datos['descuento']*100)}%")

while True:
    producto = input("\nIngrese el producto que desea comprar (o 'salir' para terminar): ").lower()
    
    if producto == "salir":                         # ERROR 9
        break
    
    if producto not in productos:                # ERROR 10
        print("❌ Producto no disponible.")
        continue
    
    try:
        # ERROR 11
        cantidad = int(input(f"Ingrese la cantidad de {producto} que desea comprar: "))
    except ValueError:
        print("⚠️ Ingrese un número válido.")
        continue

    # ERROR 12
    if cantidad <= 0:
        print("⚠️ La cantidad debe ser mayor que cero.")
        continue
    
    # ERROR 13
    if cantidad > productos[producto]["stock"]:
        print("⚠️ No hay suficiente stock disponible.")
        continue
    
    # Calcular valores con descuento
    # ERROR 14
    precio_unit = productos[producto]["precio_unit"]
    descuento = productos[producto]["descuento"]
    subtotal = precio_unit * cantidad
    descuento_valor = subtotal * descuento
    subtotal_desc = subtotal - descuento_valor
    iva = subtotal_desc * 0.19     # ERROR 15
    total = subtotal_desc + iva
    
    # Guardar en el carrito
    carrito.append((producto, cantidad, subtotal, descuento_valor, subtotal_desc, iva, total))  # ERROR 16
    
    # Actualizar stock
    productos[producto]["stock"] -= cantidad   # ERROR 17 
    print(f"✅ {cantidad} {producto}(s) agregado(s) al carrito con {int(descuento*100)}% de descuento.")

# Mostrar resumen de compra
print("\n🧾 Resumen de compra:")
total_general = 0   # ERROR 19
total_items = 0
# ERROR 18
for prod, cant, sub, desc, subdesc, iva, tot in carrito:
    print(f"{prod.capitalize()} | Cantidad: {cant} | Subtotal: {sub} | Descuento: {desc:.2f} | Subtotal c/desc: {subdesc:.2f} | IVA: {iva:.2f} | Total: {tot:.2f}")
    total_general += tot
    total_items += cant

print(f"\n🛍️ Total de productos comprados: {total_items}")
print(f"💰 Total a pagar (con IVA incluido): {total_general:.2f}")  # ERROR 20
print("✅ Gracias por su compra, vuelva pronto.")
