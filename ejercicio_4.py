# Ejercicio 4 (18 puntos): Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

def main():
    lista_asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]

    # variable[inicio:final:intervalo]
    for i in range(len(lista_asignaturas)-1,-1,-1):
        ingreso = int(input("# Ingrese la nota de la asignatura '" + lista_asignaturas[i] + "': "))
        if ingreso >= 40:
            lista_asignaturas.pop(i)
    
    print("Asignatura/s reprobada/s: "+ str(lista_asignaturas))
     
if __name__ == '__main__':
    main()

'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''