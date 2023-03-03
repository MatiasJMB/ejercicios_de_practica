'''
                  Matías Moreno Barrios
┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿   Cristian Antezana Pizarro
'''  
import random

# Genera una piedra papel o tijera para la computadora
# piedra = 1
# papel  = 2
# tijera = 3
def generar_aleatorio():
    aleatorio = random.randint(1, 3)
    return aleatorio

# Converierte los numeros 1, 2 o 3 a piedra, papel o tijera
def convierte(numero):
    if numero == 1:
        mano = "piedra"
    elif numero == 2:
        mano = "papel"
    else:
        mano = "tijera"
    return mano

# Dedice quien gana: devuelve 1 si gana la mano 1, 
# devulve 2 si gana la mano 2, 
# devulve 3 si hay empate.
def quien_gana(mano1, mano2):
    resultado = 0
    if mano1 == "piedra":
        if mano2 == "piedra":
            resultado = 3
        elif mano2 == "papel":
            resultado = 2
        elif mano2 == "tijera":
            resultado = 1

    elif mano1 == "papel":
        if mano2 == "piedra":
            resultado = 1
        elif mano2 == "papel":
            resultado = 3
        elif mano2 == "tijera":
            resultado = 2
    
    else:
        if mano2 == "piedra":
            resultado = 2
        elif mano2 == "papel":
            resultado = 1
        elif mano2 == "tijera":
            resultado = 3

    return resultado
    

def main(): 
    bienvenida = """
Bienvenido al Menú, escoja 

1) piedra
2) papel 
3) tijera
Sólo ingrese números enteros!
        """
    print(bienvenida)

    computador = 0
    jugador = 0
    empates = 0

    while True:
        respuesta = input("Desea jugar? (s/n) ")
        # Sólo se juega si dice "s", de otro modo hace break y muestra los contadores de resultados
        if respuesta == "s":
            resultado = 0

            #Se genera una elección para el computador
            aleatorio = generar_aleatorio()
            mano_computador = convierte(aleatorio)
            

            # Se recibe la elección del jugador y se everifica que sea mayor o igual a 1 y 
            # menor o igual a 3
            while True:
                intento = int(input("Ingrese piedra, papel, o tijera: "))
                if intento >= 1 and intento <= 3:
                    #El número elegido se convierte en texto (piedra, papel, o tijera)
                    mano_jugador = convierte(intento)
                    print("El jugador eligió: " + mano_jugador)
                    print("El computador jugó: " + mano_computador)

                    #Se decide quien gana
                    resultado = quien_gana(mano_computador, mano_jugador)

                    #Se guanda el resultado en contadores
                    if resultado == 1:
                        computador += 1
                        print("Ganó el computador.")
                    elif resultado == 2:
                        jugador += 1
                        print("Ganó el jugador.")
                    elif resultado == 3:
                        empates += 1
                        print("Hubo un empate.")  
                    break # Éste ´break´ permite que el flujo del programa salga del while anidado y el flujo
                          #salte al 'while' que pregunta si 'desea jugar nuevamente' 
                else:
                    continue # Con este 'continue' se le pide al usuario que ingrese nuevamente un número 
                             # ya que el que ingresó estaba fuera del rango permitido.        
        else:
            break # Si a la pregunta 'desea jugar', el jugador contesta algo distinto a 's', entoces
                  # el flujo se sale del 'while' principal, y se muestran los contadores

    # Imprime los contadores históricos
    print("El computador ganó: " + str(computador ))
    print("El jugador ganó: " + str(jugador ))
    print("Empates: " + str(empates ))





if __name__ == '__main__':
    main()
