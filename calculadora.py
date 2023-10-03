#definir la funcion número de datos ingresados
def numeroDatos(lista):
    numeroDatos = len(lista)
    return numeroDatos

#Los números ingresados ordenados de menor a mayor
def numerosOrden(lista):
    numerosOrden = sorted(lista)
    return numerosOrden

# La suma de los datos ingresados
def suma(lista):
    suma = sum(lista)
    return suma

#El promedio de los valores ingresados
def promedio(lista):
    promedio = sum(lista)/numeroDatos(lista)
    return promedio

#La mediana de los datos ingresados
def mediana(listaOrdenada):
    numDatos = numeroDatos(lista)
    listaOrdenada = numerosOrden(lista)
    if numDatos % 2 == 0:
        mediana = (listaOrdenada[int((len(listaOrdenada)-1)/2)] + listaOrdenada[int((len(listaOrdenada)-1)/2)+1])/2
    else:
        mediana = listaOrdenada[int((len(listaOrdenada)-1)/2)]
    return mediana

# La moda de los datos ingresados
def modaDatos(lista):
    listaOrdenada = numerosOrden(lista)
    moda = listaOrdenada[0]
    modeTimes = 0
    checkingValues = listaOrdenada[0]
    checkingTimes = 0
    for i in range(0, len(listaOrdenada)):
        if checkingValues == listaOrdenada[i]:
            checkingTimes += 1
        else:
            if checkingTimes > modeTimes:
                moda = checkingValues
                modeTimes = checkingTimes
                checkingValues = listaOrdenada[i]
                checkingTimes = 1
        
            else:
                checkingValues = listaOrdenada[i]
    if checkingTimes > modeTimes:
                moda = checkingValues
                modeTimes = checkingTimes

    return moda, modeTimes

#definir el valor máximo de la lista
def max(lista):
     listaOrdenada = numerosOrden(lista)

# definir la varianza

def varianza(lista):
    n = numeroDatos(lista)
    mean_v = promedio(lista)
    numero = 0
    for i in lista:
         numero += (i-mean_v)**2
         var = numero/n
    return var

# definir la desviacion standard

def stdv(lista):
     var_v = varianza(lista)
     stdv_v = (var_v)**(1/2)
     return stdv_v

# lista = [2,3,4,4]

# realizar la media geométrica

def mediaGeo(lista):
    n = numeroDatos(lista)
    product = 1
    for i in lista:
         product *= (i)
    mediaGeo_v = product**(1/n)
    return mediaGeo_v

def menu():
    print("bienvenido a la calculadora de datos")
    lista = input("ingrese una lista de numeros separados por coma:")
    listaStr = (lista.split(","))
    parameters = [int(y) for y in listaStr]

    numerodeDatos = numeroDatos(parameters)
    orden = numerosOrden(parameters)
    sumaDatos = suma(parameters)
    Promedio = promedio(parameters)
    Mediana = mediana(parameters)
    Moda = modaDatos(parameters)
    Máximo = max


menu()
#listaOrdenada= numerosOrden(lista)
#modaDatos(lista)
'''
print(modaDatos(lista))
print(varianza(lista))
print(stdv(lista))
print(mediaGeo(lista))
'''


