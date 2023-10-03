numeroA = 4
numeroB = 6
MCM = 1

while not(MCM % numeroA == 0 and MCM % numeroB == 0):
    MCM += 1

print(f''' el minino comum multiplo de {numeroA} y {numeroB} es {MCM}''')
