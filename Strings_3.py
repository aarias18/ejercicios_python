name = "camino"
nameInitial = name[0]
nameUpper = nameInitial.upper()
finalName = name.replace(nameInitial, nameUpper)
lenght = len(name)
lastName = name[lenght-1]
lastNameUp =lastName.upper()
FinalNameR = finalName.replace(lastName, lastNameUp)
print(FinalNameR)