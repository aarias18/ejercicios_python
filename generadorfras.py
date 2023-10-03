import random
Myname = input("write your name")
ListA = ["alto", "delgado", "sonriente", "amable"]
ListB = ["jirafa", "culebra", "coneja", "cangura"]
ListC = ["comer", "correr", "caminar", "dormir"]

print(f"!{Myname} es tan {ListA[random.randint(0,len(ListA)-1)]} como una {ListB[random.randint(0,len(ListB)-1)]} y debe {ListC[random.randint(0,len(ListC)-1)]} mas!")