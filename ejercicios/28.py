#ejercicio 28: Simulación de alarma
temperatura = 39
humedad = 85
alarma = (temperatura < 0 or temperatura > 38) and (humedad > 80)
print("Alarma activada:", alarma)
