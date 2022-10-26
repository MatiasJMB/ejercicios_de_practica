# Localizar el error en el siguiente bloque de codigo. Crea una excepcion para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

"""
colores = {'rojo':'red', 'verde':'green', 'negro':'black'}
colores['blanco']
"""

def main():
    try:
        colores = {'rojo':'red', 'verde':'green', 'negro':'black'}
        colores['blanco']
    except KeyError:
        print("Error: El elemento del diccionario al cual se quiere acceder no existe.")
    

if __name__ == '__main__':
    main()