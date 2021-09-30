# CICLOS WHILE O MIENTRAS
print("==========CICLOS WHILE O MIENTRAS O ITERACIONES============")
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
print("==========ESTRUCTURA WHILE============")
# <literal o contador> = 0
# while <condicion>:
#   <lo que se ejecuta si es verdadera la condicion>
#   <literal o contador> = <literal o contador> + 1
contador = 1
while contador <= 10:
  print(f"voy en numero {contador}")
  contador = contador + 1
  # contador += 1
print("*********************** BREAK *************************")
contador = 1
while contador <= 10:
  if contador == 8:
    print("-------------------LLEGUE AL 8 DEBO SALIR >.<")
    break
  print(f"voy en numero {contador}")
  contador += 1
print("*********************** CICLOS ANIDADOS *************************")
contador_interno = 1
contador_externo = 1
while contador_externo <= 10:
  print(f"voy en numero while externo {contador_externo}")
  while contador_interno <= 10:
    print(f"voy en numero while externo {contador_interno}")
    contador_interno += 1
  contador_externo += 1