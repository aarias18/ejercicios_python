sumaFinal = input("write the sum")
#buscar el "+"
findPlus = sumaFinal.find("+")
#buscar el primer numero
firstNumber = sumaFinal[0 : findPlus]
#buscar longitud
longitud = len(sumaFinal)
#buscar el segundo numero
secondNumber = sumaFinal[findPlus+1: longitud]
#transformar a numeros
firtNumberInt = int(firstNumber)
secondNumberInt = int(secondNumber)
print(firtNumberInt + secondNumberInt)