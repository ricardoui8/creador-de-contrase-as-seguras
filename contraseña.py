# ********* CREADOR SEGURO DE CONTRASEÑAS *********

caracteres = int(input("Ingrese el número de caracteres: "))
numeros = input("¿Desea que su contraseña contenga números? (si/no): ")
mayusculas = input("¿Desea que su contraseña tenga mayúsculas? (si/no): ")
caracterespecial = input("¿Desea que su contraseña tenga caracteres especiales? (si/no); ")

numeros = numeros.lower()
if numeros == "si":
    bancocaracteres = bancocaracteres + "0123456789"
  
mayusculas = mayusculas.lower()
if mayusculas == "si":
    bancocaracteres = bancocaracteres + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

caracterespecial = caracterespecial.lower()
if caracterespecial == "si":
  bancocaracteres = bancocaracteres + ".,+}{][)(?¡¿#$%&/"
  
contrasena = ""
contador = 0

while contador < caracteres:
    numerocaracteres = length(bancocaracteres)
    caracteraleatorio = floor(random * numerocaracteres) 
    contrasena = contrasena + bancocaracteres[caracteraleatorio]
    contador = contador + 1
print("Tu contraseña segura es:", contrasena)
