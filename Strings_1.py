textoString = "Me encanta Python!"
length = len(textoString)
upper_text = textoString.upper()
lower_text = textoString.lower()
sliced_text = textoString[0:6]
replaced_text = textoString.replace("Python", "JavaScript")
print(f'''Su frase tiene {length} caracteres. Aquí está en mayúsculas: {upper_text} y aquí está en minúsculas: {lower_text}. Estos son los primeros 5 caracteres de su frase: {sliced_text}. Esta es su frase sin la palabra Python: {replaced_text}''')

