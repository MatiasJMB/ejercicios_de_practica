# Crear una función que tome una lista de palabras y devuelva la frase que forma. 
# Por ejemplo ['hola','mundo','python'] corresponde a la frase "hola mundo python".

from functools import reduce

def lista_a_frase(lista):
    resultado = reduce(lambda a, b: a + " " + b, lista)
    return resultado

def main():
    lista_palabras = ['hola','mundo','python', 'juan', 'perez']
    print( lista_a_frase(lista_palabras) )

if __name__ == '__main__':
    main()