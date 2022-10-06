# Ejercicio 2 (18 puntos): Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes: (IMAGEN ADJUNTA). Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar.

def main():
    renta = int(input("# Ingresar renta anual: "))
    if (renta < 10000):
        impuesto = (renta * 5) / 100
    elif (renta >= 10000 and renta < 20000):
        impuesto = (renta * 15) / 100
    elif (renta >= 20000 and renta < 35000):
        impuesto = (renta * 20) / 100
    elif (renta >= 35000 and renta < 60000):
        impuesto = (renta * 30) / 100
    else:
        impuesto = (renta * 45) / 100

    print("Valor renta a pagar: " + str(impuesto))

if __name__ == '__main__':
    main()
    
'''
¯\_( ͡° ͜ʖ ͡°)_/¯ Matias Moreno Barrios
'''