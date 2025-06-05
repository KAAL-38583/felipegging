#ejercicio 10: Máximo entre tres números
a = 5
b = 10
c = 7
if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c
print("El mayor es:", max_num)
