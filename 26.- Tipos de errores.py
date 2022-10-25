# Errores de sintaxis es cuando yo escribo algo y no es reconocido:
# Ej:
# print("Hola")) <-- El mismo Visual te avisa el error, como este parentesis demás.

# Tambien podemos tener errores de lógica en ejercicios matematicos.
# Como una division entre 0:
# print(0/0)

# Otro error seria el de variable NO definida. (suma no está definida):
# print(suma)

# Error assertion - Error de afirmacion
# Me permite tomar una condicion y validarla manualmente. Me permite determinar si mi duncion está haciendo lo que le estoy pidiendo.
# suma = lambda x, y: x + y
# assert suma(1,2) == 5
# assert: comprueba que la condicion es verdadera, si no lo es genera un error.

# Generar nuestro porpio error - excepción propia. Nos sirve para controlar mejor los errores.
edad = 17
if edad < 18:
    raise Exception("El usuario es menor de edad")
else:
    print("El usuario es mayor de edad")