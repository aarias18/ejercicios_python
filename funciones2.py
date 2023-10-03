import random

def captureSelection():
    list = input(piedra,papel,tijera)
    RamdomSelection = (piedra,papel,tijera)
    return 
    


Myoption = input("ingrese una opción")
list = ["piedra","papel","tijera"]
RamdomSelection = list[random.randint(0, len(list)-1)]
#print(RamdomSelection)
if Myoption == RamdomSelection:
    print(f"es un emapate porque usted sacó {Myoption} y la maquina sacó {RamdomSelection}")
else:
    if Myoption == "tijera":
        if RamdomSelection == "piedra":
            print(f"usted perdio por que usted eligió {Myoption} y la máquina sacó {RamdomSelection}")
        else:
            print(f"usted ganó por que usted eligió {Myoption} y la máquina sacó {RamdomSelection}")
    elif Myoption == "piedra":
        if RamdomSelection == "papel":
            print(f"usted perdio por que usted eligió {Myoption} y la máquina sacó {RamdomSelection}")
        else:
            print(f"usted ganó por que usted eligió {Myoption} y la máquina sacó {RamdomSelection}")
    elif Myoption == "papel":
        if RamdomSelection == "piedra":
            print(f"usted ganó por que usted eligió {Myoption} y la máquina sacó {RamdomSelection}")
        else:
            print(f"usted perdió por que usted eligió {Myoption} y la máquina sacó {RamdomSelection}")
