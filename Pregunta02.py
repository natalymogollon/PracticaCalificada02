# Una historia de usuario es un breve resumen de una actividad a realizarse en programación

# Sirve para optimizar el tiempo de entendimiento acerca de lo que se está planteando resolver

# Ejemplo:

# Historia: Realizar un programa de almacenamiento de datos
# Como: Programador me gustaría saber cuales son los datos a ingresar a traves del programa 
# Quiero: mostrar en una pantalla la inforamcion que el usuario ingrese en el programa

cantidad = int(input("Ingrese cantidad de personas a ingresar: "))
for i in range(cantidad):
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    carrera = input("Ingrese nombre de su carrera: ")

