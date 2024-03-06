def calcular_precio_venta(precio_costo):
    if precio_costo < 3000:
        ganancia = precio_costo * 0.15
    elif 3000 <= precio_costo <= 6000:
        ganancia = 500
    else:
        ganancia = precio_costo * 0.25
    
    precio_venta = precio_costo + ganancia
    return precio_venta

precio_costo = float(input("Ingrese el precio de costo del artículo: "))
precio_venta = calcular_precio_venta(precio_costo)
print("El precio de venta del artículo es:", precio_venta)
