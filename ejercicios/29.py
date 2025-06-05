#ejercicio 29: Contraseña segura
password = "abc12345"
es_segura = len(password) > 8 and any(char.isdigit() for char in password)
print("Contraseña segura:", es_segura)
