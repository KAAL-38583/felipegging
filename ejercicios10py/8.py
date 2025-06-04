# Ejercicio 8: Número mayor
# Descripción: Pide tres números al usuario y muestra cuál es el mayor.
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
mayor = max(a, b, c)
print(f"El número mayor es: {mayor}")