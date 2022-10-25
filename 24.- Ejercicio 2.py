# Crear una función que retorne las palabras de una lista de palabras que comience con una letra en especifico.

def filtro_palabras(lista_palabras, letra):
    resultado = filter(lambda palabra: palabra[0] == letra, lista_palabras)
    return list(resultado)

def main():
    palabras = ['Perro', 'Gato', 'Pelota', 'Manzana', 'Libro', 'Python', 'Guante']
    letra_busqueda = 'G'

    palabras_filtradas = filtro_palabras(palabras, letra_busqueda)
    print(palabras_filtradas)

if __name__ == '__main__':
    main()