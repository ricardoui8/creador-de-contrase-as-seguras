#********* CREADOR SEGURO DE CONTRASEÑAS *********

import random

caracteres = int(input("Ingrese el número de caracteres: ").lower())
numeros = input("¿Desea que su contraseña contenga números? (si/no): ").lower()
mayusculas = input("¿Desea que su contraseña tenga mayúsculas? (si/no): ").lower()
caracterespecial = input("¿Desea que su contraseña tenga caracteres especiales? (si/no); ").lower()

bancocaracteres = ("abcdefghijklmnopqrstuvwxyz")

if numeros == "si":
    bancocaracteres = bancocaracteres + ("0123456789")
  
if mayusculas == "si":
    bancocaracteres = bancocaracteres + ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

if caracterespecial == "si":
  bancocaracteres = bancocaracteres + (".,+}{][)(?¡¿#$%&/")
  
contrasena = ""
for i in range(caracteres):
    caracteres_aleatorio = random.choice(bancocaracteres)
    contrasena = contrasena+caracteres_aleatorio
print("Tu contraseña segura es:" + contrasena)

    contador = contador + 1
print("Tu contraseña segura es:"+ contrasena)
