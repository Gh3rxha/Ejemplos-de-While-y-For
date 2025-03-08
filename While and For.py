# código de Python con While and For.

import random
import time

productos = [
    {"nombre": "Laptop", "stock": 5, "precio": 1000},
    {"nombre": "Teléfono", "stock": 8, "precio": 500},
    {"nombre": "Tablet", "stock": 4, "precio": 300},
    {"nombre": "Monitor", "stock": 6, "precio": 200},
]

while any(producto["stock"] > 0 for producto in productos):
    print("\n--- Inventario de la tienda ---")
    for i, producto in enumerate(productos):
        print(f"{i + 1}. {producto['nombre']}: Stock {producto['stock']} - Precio ${producto['precio']}")
    
    while True:
        opcion = input("\nIngrese el número del producto que desea comprar (o '0' para salir): ")
        
        if opcion == '0':
            print("Gracias por visitar la tienda. Hasta luego!")
            exit()
        
        if not opcion.isdigit() or int(opcion) not in range(1, len(productos) + 1):
            print("Error: Número fuera de las opciones disponibles. Intente nuevamente.")
            continue
        
        break
    
    indice = int(opcion) - 1
    
    while True:
        cantidad = input(f"¿Cuántas unidades de {productos[indice]['nombre']} desea comprar? ")
        
        if not cantidad.isdigit() or int(cantidad) <= 0:
            print("Cantidad no válida. Intente nuevamente.")
            continue
        
        cantidad = int(cantidad)
        
        if productos[indice]["stock"] >= cantidad:
            productos[indice]["stock"] -= cantidad
            print(f"Has comprado {cantidad} {productos[indice]['nombre']}(s). ¡Gracias por tu compra!")
        else:
            print("Lo sentimos, no hay suficiente stock disponible.")
            continue
        
        break
    
    while True:
        seguir_comprando = input("¿Desea comprar algo más? (s/n): ").strip().lower()
        if seguir_comprando in ['s', 'n']:
            break
        print("Por favor, ingrese 's' para sí o 'n' para no.")
    
    if seguir_comprando == 'n':
        print("Gracias por su compra. Hasta luego!")
        break
    
    time.sleep(1)

print("\nTodos los productos están agotados o la tienda ha cerrado.")
