#ejercicio 20: Detección de tipo
x = 10.5
if isinstance(x, int):
    tipo = "int"
elif isinstance(x, float):
    tipo = "float"
elif isinstance(x, str):
    tipo = "str"
else:
    tipo = "otro"
print("El tipo de x es:", tipo)
