print("Ejercicio1 (Uso de Conjuntos)...")

#Crea un conjunto llamado usuarios con usuarios Marta, David, Elvira, Juan y Marcos:
usuarios={"Marta","David","Elvira","Juan","Marcos"}

#Crea otro con usuarios admin Juan y Marta:
administradores={"Juan","Marta"}
# Borra a Juan de admin
administradores.remove("Juan")
#Añade a Marcos como admin:
administradores.add("Marcos")

print(usuarios)
print(administradores)

for nombre in usuarios:
    if nombre in administradores:
        print(nombre," Es un usuario admin")
    else:
        print(nombre," No es un usuario admin")
     

print("\nEjercicio2 (Uso de diccionarios)...")
#Durante el desarrollo de un videojuego, se te encarga configurar y balancear cada clase de personaje jugable.
#Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

caballero={"vida":2,"ataque":2,"defensa":2,"alcance":2}
guerrero={"vida":2,"ataque":2,"defensa":2,"alcance":2}
arquero={"vida":2,"ataque":2,"defensa":2,"alcance":2}

#El caballero tiene el doble de vida que un guerrero:
caballero["vida"]=guerrero["vida"]*2
caballero["defensa"]=guerrero["defensa"]*2

#el guerrero tiene el doble de ataque y el doble de alcance que un caballero:
guerrero["ataque"]=caballero["ataque"]*2
guerrero["alcance"]=caballero["alcance"]*2

#Arquero=vida y ataque que guerrero --- mitad de defensa y doble de su alcance:
arquero["ataque"]=guerrero["ataque"]
arquero["vida"]=guerrero["vida"]
arquero["defensa"]=guerrero["defensa"]/2
arquero["alcance"]=guerrero["alcance"]*2

#Mostrar resultados:
print("Caballero:\t",caballero)
print("guerrero:\t",guerrero)
print("arquero:\t",arquero)


print("\nEjercicio3 (Uso de Colas)...")
#Durante la planificación de un proyecto se han acordado una lista de tareas.
#Para cada una de las tareas se ha asignado un orden de prioridad (cuanto menor es el número, más prioridad).
#¿Eres capaz de crear una estructura de tipo cola con todas las coordenadas pero sin los números de orden?:

tareas = [ 
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("==Tareas desordenadas==")
for tarea in tareas:
    print(tarea[0], tarea[1])

from collections import deque

tareas.sort # ordenar una lista
print(tareas)

cola=deque()
for tarea in tareas:
    cola.append(tarea[1])

print("==Tareas ordenadas==")
for tarea in cola:
    print(tarea)

