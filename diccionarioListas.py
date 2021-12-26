#Ejemplo utilizando diccionarios y listas a la vez
# Podemos crear nuestras propias estructuras avanzadas mezclando ambas colecciones. Mientras los diccionarios se encargarían de 
# manejar las propiedades individuales de los registros, las listas nos permitirían manejarlos todos en conjunto.

# Creación de la lista/array
personajes = []

# Creacióm del diccionario
p = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'}  

#añadir un valor:valor ---- p["perro"] = "dog"

personajes.append(p) # NombreLista.append --- para añadir valores
print(personajes)
p = {'Nombre':'Legolas','Clase':'Arquero','Raza':'Elfo'}
personajes.append(p)
p = {'Nombre':'Gimli','Clase':'Guerrero','Raza':'Enano'}
personajes.append(p)
print(personajes)

for p in personajes:
    print(p['Nombre'], p['Clase'], p['Raza'])

print("Fin del programa")