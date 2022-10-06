# Ejercicio 3 (18 puntos): Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def main():
    print("# Para terminar ingrese 'salir'\n")
    cadena = str()
    while (cadena != "salir"):
        cadena = input("Ingrese una cadena de texto: ")
        if (cadena == "salir"):
            print("Programa finalizado.")
        else:
            print("⮕ Texto ingresado: " + cadena)
    
if __name__ == '__main__':
    main()
    
'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''