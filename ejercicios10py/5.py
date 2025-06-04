# Ejercicio 5: Intercambiar valores entre dos variables
# Descripción: Intercambia los valores de dos variables sin usar una tercera variable
x = input("Ingresa el valor de x: ")
y = input("Ingresa el valor de y: ")
x, y = y, x
print(f"Ahora x es: {x} y y es: {y}")