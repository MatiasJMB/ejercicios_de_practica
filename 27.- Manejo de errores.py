# Con esto podremos evitar que nuestro codigo se detenga cuando haya un error.

from logging import exception
from typing import final


# try:
#     print(1 / 2)
    
# except ZeroDivisionError as error:
#     print("Error: Se está intentando dividir entre 0.")
#     print(error)

# print("Hola mundo")


# try:
#     assert 1 != 1
    
# except AssertionError as error:
#     print(error)
    
# try:
#     edad = 17
#     if edad < 18:
#         raise Exception("El usuario es menor de edad")
# except Exception as error:
#     print(error)
    
# Simplificado del codigo:
try:
    print(1 / 2)
    assert 1==1
    edad = 17
    if edad < 18:
        raise Exception("El usuario es menor de edad")

except ZeroDivisionError as error:
    print("Error: Se está intentando dividir entre 0.")
    print(error)
except AssertionError as error:
    print("Assertion error mensaje")
    print(error)
except Exception as error:
    print(error)
else:
    print("Es mayor de edad")
finally:
    print("El programa terminó")