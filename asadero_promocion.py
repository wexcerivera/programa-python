
# Matriz con los productos
menu = [
    ["Pechuga de Pollo", "Carnes", 22000],
    ["Costilla de Res", "Carnes", 28000],
    ["Chorizo Artesanal", "Carnes", 12000],
    ["Parrillada Mixta", "Parrilladas", 45000],
    ["Papas a la Francesa", "Acompanamientos", 8000],
    ["Limonada Natural", "Bebidas", 5000]
]

# Reglas de la promocion
categoria_objetivo = "Carnes"
umbral_precio = 15000

# Funcion para calcular precio final
def calcular_precio_final(categoria, precio_base):
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        return precio_base * 0.85
    else:
        return precio_base

# Mostrar informe
print("INFORME DE PRECIOS - ASADERO SUPER POLLO")
print("=" * 50)
print("Producto          | Categoria       | Precio Base | Precio Final")
print("-" * 50)

for producto in menu:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]
    
    precio_final = calcular_precio_final(categoria, precio_base)
    
    # Mostrar si aplica o no descuento
    if precio_final != precio_base:
        estado = "CON descuento"
    else:
        estado = "SIN descuento"
    
    print(f"{nombre:<16} | {categoria:<14} | ${precio_base:>8} | ${precio_final:>8} | {estado}")

print("-" * 50)
print("Descuento del 15% aplica a productos de categoria 'Carnes'")
print("cuyo precio base sea mayor a $" + str(umbral_precio))
print()
input("Presiona ENTER para salir...")