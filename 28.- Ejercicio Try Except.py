# Ejercicio 1:
# Creear una función que divida dos numeros y los retorne. La funcion debe ser capaz de enviar un mensaje si se ingresa un valor no válido o matematicamente imposible, en el caso de haber error devolver un numero 0.

def dividir(valor1, valor2):
    
    try:
        calculo = (valor1 / valor2)
    except ZeroDivisionError:
        print("Error: se está tratando de dividir entre 0.")
        calculo = 0
    except TypeError:
        print("Error: uno de los valores ingresados no es valido.")
        calculo = 0
    except Exception as e:
        print("Ocurrió un error:")
        print(e)
        calculo = 0
    finally:
        return calculo

def main():
    resultado = dividir(1,[2])
    print(resultado)

if __name__ == '__main__':
    main()