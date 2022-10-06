# Ejercicio 1 (18 puntos): Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato en la consola y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

def main():
    print("# Ingresa tu numero de telefono con el siguiente formato:")
    print("(prefijo-número-extensión) | Ej: +34-913724710-56")
    telefono = input("Ingrese un número de teléfono: ")
    solo_numero = telefono[4:-3]
    print(solo_numero)

if __name__ == '__main__':
    main()
    
'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''