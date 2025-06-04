# Ejercicio 9: Verificar si un número es múltiplo de otro
# Descripción: Pide dos números y determina si el primero es múltiplo del segundo.
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
if b == 0:
    print("Error: No se puede dividir entre cero")
elif a % b == 0:
    print(f"{a} es múltiplo de {b}")
else:
    print(f"{a} no es múltiplo de {b}")