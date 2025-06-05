#ejercicio 22: Control de acceso lógico
tiene_pase_vip = False
paga_entrada = True
esta_ebria = False
puede_entrar = tiene_pase_vip or (paga_entrada and not esta_ebria)
print("Puede entrar:", puede_entrar)
