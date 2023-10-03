def determinaIMC(masa,altura):
    determinaIMC = masa / (altura * altura)
    return determinaIMC

def rangos(IMCf):
    if IMCf >= 16 and IMCf <= 22:
        print("usted esta bajo de peso, debe consumir mas alimentos")
    elif IMCf > 22 and IMCf <=25:
        print("usted tiene un peso normal, felicitaciones")
    elif IMCf > 25:
        print("usted tiene sobrepseo, por favor acuda a un nutricionista")

masa = float(input(" ingrese su peso en kilogramos "))
altura = float(input(" ingrese su altura en metros "))

#print(f'''su indice de masa corporal es {determinaIMC}''')
IMCf = determinaIMC(masa,altura)

rangos(IMCf)


print(f'''su peso en Kg es {masa}, su altura en metros es {altura}, y su indice de masa corporal IMC es {IMCf}''')