# Reduce

# Aplica una funcion a una lista y devuelve un único valor

from functools import reduce

def main():
    # Forma tradicional
    lista = [1, 2, 3, 4, 5]
    producto = 1
    for numero in lista:
        producto = producto * numero
    print(producto)

    # Forma con reduce
    lista = [1, 2, 3, 4, 5]
    producto = reduce(lambda a, b: a * b, lista)
    print(producto)

if __name__ == '__main__':
    main()