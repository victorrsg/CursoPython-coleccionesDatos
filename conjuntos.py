# Variables del ejercicio (no las modifiques)
grupo = {"Miguel", "Blanca", "Mario", "Andrés"}
 
# Completa el ejercicio
grupo.add("Ana")
grupo.add("Ramón")
grupo.add("Marta")
grupo.add("Eric")
grupo.add("David")

if "Miguel" in grupo:
    print(True)

grupo.remove("Mario")
grupo.remove("Miguel")
grupo.remove("Ramón")


#Eliminar los valores repetidos de un array:
array=[1,2,3,3,2,1]
print(array)
c=set(array) #Transformamos nuestro array en un conjunto con set()
print(c)
array=list(c) #Transformamos el conjunto a un array con list()
print(array)

print("-----------------")
#Otra forma más interesante: 
array=[1,2,3,3,2,1]

array=list(set(array))
print(array)