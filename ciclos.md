# CICLOS
Los bucles, en diversos lenguajes de programación pueden ser definidos o indefinidos. Los bucles definidos preestablecen las condiciones de la iteración por adelantado. Por su parte, los bucles indefinidos establecen la condición en la que una iteración terminará. En este último tipo de bucles existe el riesgo de que el bucle se vuelva infinito (cuando la condición de suspensión nunca se cumple).

Los bucles definidos se implementan en Python a través del keyword for. Por su parte, los bucles indefinidos se implementan con el keyword while.

Sin embargo, esta no es la única forma de implementar bucles definidos. Por ejemplo, Javascript puede implementar un bucle definido mediante el siguiente constructo:
## CICLOS INDEFINIDOS JAVASCRIPT
```javascript
while(a < b){
  <expresión>
}
```
## CICLOS INDEFINIDOS PYTHON
```python
contador = 1
while contador <= 10:
  print(f"voy en numero {contador}")
  contador = contador + 1
  # contador += 1
```

## CICLOS DEFINIDOS JAVASCRIPT
```javascript
for (i = 0; i <= 10; i++) {
  <expresión>
}
```
## CICLOS DEFINIDOS PYTHON
```python
nombre = "jack"
for letra in nombre:
  print(f"vamos en la letra: {letra}")
```



