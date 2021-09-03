print("==========Inicio de mi codigo python============")
# # SIRVE PARA DOCUMENTAR O COMENTAR NUESTRO CODIGO
# print sirve para imprimir en consola
print("1. Hola mi primera imprecion en consola")
# Elementos básicos de Python
# <literales> = 1 'hola' 4.0 True, False
# <operadores> = + / * % ** = ==
# <literales> <operadores> <literales>
# Asignacion de datos
base = 5
saludo = "hola"
primer_saludo = 'hola'
pi = 3.1416
es_mayor = True
es_menor = False
print("==============BASE==============")
print(base)
print("==============SALUDO==============")
print(saludo)
print("==============PRIMER_SALUDO==============")
print(primer_saludo)
print("==============PI==============")
print(pi)
print("==============ES_MAYOR==============")
print(es_mayor)
print("==============ES_MENOR==============")
print(es_menor)
# utilizacion metodo type()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(type(base))
print("============================")
print(type(saludo))
print("============================")
print(type(primer_saludo))
print("============================")
print(type(pi))
print("============================")
print(type(es_mayor))
print("============================")
print(type(es_menor))
print("============================")
# CONCATENACION
print("Jack "+"Florez Jimenez")
print(primer_saludo+" jack")
# INTERPOLACION
print("==============INTERPOLACION==============")
print(f"{primer_saludo} jack cual es el valor del numero pi: {pi}")
# METODOS DE CADENAS
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
nombre_completo_profesor = "Jackson Edward Florez Jimenez"
print("METODO DE CADENA len")
# len (longitud) total de caracteres
print(len(nombre_completo_profesor))
print("Notacion de rebanadas o Slicing ")
#                            0123456789..................28
#nombre_completo_profesor = "Jackson Edward Florez Jimenez"
print("Traigo la letra en la 8 posicion deberia ser la E")
print(nombre_completo_profesor[8])
print("Traigo la letra en la 28 posicion deberia ser la z")
print(nombre_completo_profesor[28])
# string[comienzo:final:pasos]
print("Empezar desde la posicion 8 y traer hasta el final")
print(nombre_completo_profesor[8:])
print(nombre_completo_profesor[8:29])
print("Empezar desde el principio 0 y traer hasta 14")
print(nombre_completo_profesor[:14])
print(nombre_completo_profesor[0:14])
print("Empezar desde la posicion -4 he imprimir hasta el final")
print(nombre_completo_profesor[-4:])
print("Empezar desde el principio y terminar al final pero de a dos")
print(nombre_completo_profesor[::2])
print(nombre_completo_profesor[0:29:2])
# Coerción de datos String a Enteros y Enteros a String
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("COERCIÓN DE DATOS")
a = "7"
b = 7
# se convierte a A entero
c = int(a) + b
print("la suma de a+b es igual: "+str(c))
# Coerción de datos String a Float(coma flotante o decimal) y Float(coma flotante o decimal) a String
print("==="*30)
print("COERCIÓN DE DATOS")
e = "7.7"
f = 7
# se convierte a A entero
g = float(e) + f
print("la suma de e+f es igual: "+str(g))
# ENTRADAS
print("((((((((((((((((((((((((((((((((((((((((((((((((((((((((")
print("Ingresando datos con Python :D")
nombre_ingresado = input('Ingresa tu nombre: ')
print(f'el nombre ingresado por teclado fue: {nombre_ingresado}')
edad = input('Ingresa tu edad: ')
print("la edad ingresada es de:", edad)
# nota recordar que el tipo de dato devuelto por el metodo input() 
# es un string si se deseas hacer alguna operacion aritmetica se debe convertir a entero
