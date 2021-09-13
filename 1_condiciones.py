# OPERADORES LOGICOS Y DE COMPARACION
print("==========OPERADORES DE COMPARACION============")
print("***********************7 es IGUAL a 8*************************")
print(7 == 8)
print("***********************7 es DIFERENTE a 8*************************")
print(7 != 8)
print("***********************7 es MAYOR QUE 8*************************")
print(7 > 8)
print("***********************7 es MENOR QUE 8*************************")
print(7 < 8)
print("***********************7 es MAYOR O IGUAL QUE 8*************************")
print(7 >= 8)
print("***********************7 es MENOR O IGUAL QUE 8*************************")
print(7 <= 8)
print("==========OPERADORES LOGICOS============")
print("*********************** Y *************************")
print(True and True)
print("*********************** True and True *************************")
print(7 <= 8 and 7 != 8)
print("*********************** False and True *************************")
print(7 >= 8 and 7 != 8)
print("*********************** O *************************")
print(True or False)
print("*********************** True or True *************************")
print(7 <= 8 or 7 != 8)
print("*********************** False or True *************************")
print(7 >= 8 or 7 != 8)
print("*********************** LO CONTRARIO *************************")
print(not True)
print("==========ESTRUCTURA IF============")
print("*********************** FORMA 1 *************************")
# if <condicion>:
#   <lo que se ejecuta si es verdadera la condicion>
if 7 <= 8:
  print("se imprime cuando la condicion es verdadera")
print("*********************** FORMA 2 *************************")
# if <condicion>:
#   <lo que se ejecuta si es verdadera la condicion>
# else:
#   <lo que se ejecuta si es falso la condicion>
if 7 > 8:
  print("7 es mayor que 8")
else:
  print("7 es menor que 8 :D")
# if <condicion>:
#   <lo que se ejecuta si es verdadera la condicion>
# elif <condicion>:
#   <lo que se ejecuta si es falso la condicion>
# else:
#   <lo que se ejecuta si es falso la condicion>
if 7 > 8:
  print("7 es mayor que 8")
elif 7 < 8:
  print("7 es menor que 8 :D")
else:
  print("ninguna de las anteriores")
