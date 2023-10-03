name = input("write your name ")
nameInitial = name[0]
nameInitialUp = nameInitial.upper()
finalName = name.replace(nameInitial, nameInitialUp)
print(finalName)
print(name + "! Hola " + finalName + "¡", )