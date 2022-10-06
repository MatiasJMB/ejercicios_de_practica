# Ejercicio 5 (18 puntos): Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%.

def iva(cantidad_sin_iva, porcentaje):
    if (porcentaje == ''):
        porcentaje = 19
        porcentaje = int(porcentaje)

    porcentaje = int(porcentaje)
    valor_iva = cantidad_sin_iva * (porcentaje / 100)
    total = valor_iva + cantidad_sin_iva
    return total

def main():
    valor_neto = int(input("Ingrese total NETO de la factura: "))
    porcentaje_iva = str(input("Ingrese el porcentaje del IVA (EJ: 20, sin '%'): "))
    resultado = iva(valor_neto,porcentaje_iva)
    print("El total BRUTO de la factura es: $" + str(resultado))


if __name__ == '__main__':
    main()

'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''