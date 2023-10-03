numero = int(input("type and integrer number: "))
numero_print = numero
contador = int(2)

listaPrimos = ""
while contador <= numero:
    if numero % contador == 0:
        listaPrimos += str(contador)
        numero = numero / contador
    else:
        contador += 1
print(f'''Los factores primos que componen su numero son {listaPrimos}''')


