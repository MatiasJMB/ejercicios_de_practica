# Ejercicio 2
# Localizar el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explicar en un mensaje al usuario la causa y/o solución.
"""
lista = [1, 2, 3, 4, 5]
lista[10]    
"""

def main():
    try:
        lista = [1, 2, 3, 4, 5]
        print(lista[10])
    except IndexError as error:
        print("Error: El índice indicado excede el largo. Ingrese un índice válido.")
        print(error)

if __name__ == '__main__':
    main()