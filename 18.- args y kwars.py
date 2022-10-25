# *args y **kwargs

# args y kwargs pueden llevar cualquier nombre pero es una convención usarlos así, lo importante son los '*' y se utilizan para pasar un numero, variable de parametros a una función.

# *args -> argumentos | es una tupla (elemento1, elememto2, elemento3), no se pueden modificar pero si iterar
# **kwargs -> key word arguments | es un diccionario {'elemento1': valor, 'elemento2': valor}

# *args (siempre va al final)
# Argumentos que no estan asociados a un nombre
# from __future__ import division


def prueba_args(argumento, *args):
    print(argumento)
    for arg in args:
        print(arg)


prueba_args("Hola", "mundo", ["Python", "PHP", "JAVA"], 4.5, 3, True)

# **kwargs
# Argumentos que si estan asociados a un nombre
# def prueba_kwargs(**kwargs):
#     for key, value in kwargs.items:  # Con esto accedimos a los items del diccionario.
#         # print(key)
#         # print(value)
#         print("{0}: {1}".format(key, value)) # Esta es una forma distinta de imprimir los diccionarios.

# prueba_kwargs(nombre="Juan", apellido="Perez", edad=25)

# kwargs_diccionario = {
#     "arg1": 1,
#     "arg2": "DOS",
#     "arg3": 4.5
# }
# prueba_kwargs(**kwargs_diccionario)

# Ejemplo: Función que sume todos los valores que le envíe por parametros y devuelva el resultado
def suma(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total

resultado_suma = suma(1,2,3,4,5,6,7,8,9,10)
print(resultado_suma)

# Ejercicio: una funcion que reciba la operacion a realizar y los numeros a operar y devuelva el resultado

def calculadora(operacion, *args):
    if operacion == 'suma':
        total = 0
        for arg in args:
            total += arg
        return total
    elif operacion == 'resta':
        total = 0
        for arg in args:
            total -= arg
        return total
    elif operacion == 'multiplicacion':
        total = 1
        for arg in args:
            total *= arg
        return total
    elif operacion == 'division':
        total = 1
        for arg in args:
            total /= arg
        return total
    else:
        return "Operacion no válida"
            
    
resultado_calculadora = calculadora('division',2,5)            
print(resultado_calculadora)
