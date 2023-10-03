login = input("ingrese un usuario")
psw = input("ingrese una contrasena")
#longitud de contrasena
pswLong = len(psw)
if pswLong > 6 and pswLong < 10:
    print("contrasena correcta, cumple los parametros")
else:
    print("contrasena incorrecta, debe tener entrews 6 y 10 caracteres")

login = input("ingrese un usuario")
psw_1 = input("ingrese una contrasena")
psw_2 = input("ingrese una contrasena")
if psw_1 == psw_2:
    print("la validacion es correcta")
else:
    print("la validacion de la contrasena es incorrecta")