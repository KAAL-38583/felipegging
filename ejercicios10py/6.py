# Ejercicio 6: Calculadora simple
# Descripción: Realiza suma, resta, multiplicación y división con dos números ingresados por el usuario.
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}" if b != 0 else "Error: No se puede dividir por cero")
