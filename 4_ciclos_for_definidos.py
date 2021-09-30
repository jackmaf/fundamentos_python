# CICLOS FOR o para
print("==========CICLOS FOR O PARA============")
print("***********************que hacer para repetir*************************")
print("voy en numero 1")
print("voy en numero 2")
print("voy en numero 3")
print("voy en numero 4")
print("voy en numero 5")
print("voy en numero 6")
print("voy en numero 7")
print("voy en numero 8")
print("voy en numero 9")
print("voy en numero 10")
print("==========ESTRUCTURA FOR============")
# El bloque de instrucciones que se repite se suele llamar cuerpo del bucle y cada repetición se suele llamar iteración
# for <variable o auxiliar o registro en el que va> in <elemento iterable (lista, cadena, range, etc.)>:
#   <lo que se ejecuta>
print("**********Recorrer una lista o arreglo o hash*********")
print("**********EJEMPLO 1**********************************")
arreglo = [1,2,3,4,5,6,7,8,9,10]
for numero_en_el_que_voy in arreglo:
  print(f"voy en el numero {numero_en_el_que_voy}")
print("**********EJEMPLO 2**********************************")
cadena = "jack"
for letra in cadena:
  print(f"vamos en la letra: {letra}")
print("*********************** BREAK *************************")
arreglo = [1,2,3,4,5,6,7,8,9,10]
for numero_en_el_que_voy in arreglo:
  print(f"voy en el numero {numero_en_el_que_voy}")
  if numero_en_el_que_voy == 5:
    break
print("*********************** CONTINUE *************************")
arreglo = [1,2,3,4,5,6,7,8,9,10]
for numero_en_el_que_voy in arreglo:
  if numero_en_el_que_voy == 5:
    continue
  print(f"voy en el numero {numero_en_el_que_voy}")
print("*********************** CICLOS ANIDADOS *************************")
arreglo_exterior = [1,2,3,4,5,6,7,8,9,10]
arreglo_interior = ["Jack","Luis","Laura"]
for numero_ext in arreglo_exterior:
  for numero_int in arreglo_interior:
    print(f"voy en el numero {numero_int}")
  print(f"voy en el numero {numero_ext}")
print("*****************CASOS INTERESANTES*****************************")
print("*********1. Si la lista está vacía, el bucle no se ejecuta ninguna vez*****")
print("Comienzo")
for i in []:
    print("Hola ", end="")
print()
print("Final")
print("2. Si la variable de control no se va a utilizar en el cuerpo del bucle, se puede utilizar el guion (_) en vez de un nombre de variable")
cadena = "jack"
for _ in cadena:
  print("Hola")
print("3. La lista puede contener cualquier tipo de elementos, no sólo números")
print("Comienzo")
for i in ["Alba", "Benito", 27]:
    print(f"Hola. Ahora i vale {i}")
print("Final")
print("4.La costumbre más extendida es utilizar la letra i como nombre de la variable de control, pero se puede utilizar cualquier otro nombre válido")
print("Comienzo")
for numero in  [0, 1, 2, 3]:
    print(f"{numero} * {numero} = {numero ** 2}")
print("Final")
print("5. La variable de control puede ser una variable empleada antes del bucle. El valor que tuviera la variable no afecta a la ejecución del bucle, pero cuando termina el bucle, la variable de control conserva el último valor asignado")
i = 10
print(f"El bucle no ha comenzado. Ahora i vale {i}")

for i in [0, 1, 2, 3, 4]:
    print(f"{i} * {i} = {i ** 2}")

print(f"El bucle ha terminado. Ahora i vale {i}")
print("6. Cuando se escriben dos o más bucles seguidos, la costumbre es utilizar el mismo nombre de variable puesto que cada bucle establece los valores de la variable sin importar los valores anteriores:")
for i in [0, 1, 2]:
  print(f"{i} * {i} = {i ** 2}")

print()

for i in [0, 1, 2, 3]:
  print(f"{i} * {i} * {i} = {i ** 3}")

print("7. En vez de una lista se puede escribir una cadena, en cuyo caso la variable de control va tomando como valor cada uno de los caracteres:")
for i in "AMIGO":
  print(f"Dame una {i}")
print("¡AMIGO!")

print("8. En los ejemplos anteriores se ha utilizado una lista para facilitar la comprensión del funcionamiento de los bucles pero, si es posible hacerlo, se recomienda utilizar tipos range(), entre otros motivos porque durante la ejecución del programa ocupan menos memoria en el ordenador.El siguiente programa es equivalente al programa del ejemplo anterior:")
print("Comienzo")
for i in range(3):
  print("Hola ")
print()
print("Final")

print("9. Otra de las ventajas de utilizar tipos range() es que el argumento del tipo range() controla el número de veces que se ejecuta el bucle.")
print("En el ejemplo anterior basta cambiar el argumento para que el programa salude muchas más veces.")
print("Esto permite que el número de iteraciones dependa del desarrollo del programa. En el ejemplo siguiente es el usuario quien decide cuántas veces se ejecuta el bucle:")
veces = int(input("¿Cuántas veces quiere que le salude? "))
for i in range(veces):
  print("Hola ")
print()
print("Adiós")
print("10. el range(inicio, fin) se le puede colocar un rango de inicio a fin")
print("Comienzo")
for i in range(1, 6):
  print(f"vamos en {i}")
print("Fin")
print("!!!!!!!!!!!!!!!!!!!!!AVANZADO!!!!!!!!!!!!!!!!!!!!")
print("Bucles for con diccionarios")
estudiantes = {
  'mexico': 10,
  'colombia': 15,
  'puerto_rico': 4,
}
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for pais in estudiantes:
  print(f"llave izquierda o pais: {pais}")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for pais in estudiantes.keys():
  print(f"llave izquierda o pais: {pais}")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for numero_de_estudiantes in estudiantes.values():
  print(f"valor o contenido derecha: {numero_de_estudiantes}")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for pais, numero_de_estudiantes in estudiantes.items():
  print(f"valor o contenido derecha: {numero_de_estudiantes}")