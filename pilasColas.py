#Pila o stacks: ultimo que entra-primero en salir.
pila = [3,4,5]
pila.append(6)
print(pila)

print("---------")
#Sacar elementos de nuestra pila: nombrePila.pop()
n= pila.pop()
print("El valor sacado de la lista es: ",n)
print(pila)

print("-------------")


#Colas o deque: Primero en llegar primero en salir.
from collections import deque #Debemos importar el módulo deque para utilizar colas

cola = deque(['Hector','Juan','Miguel'])
print(cola)

cola.append("Maria")
print(cola)

#Sacar elementos de nuestra cola --- nombreCola.popleft()
v=cola.popleft()
print("El valor sacado de la lista es: ",v)
print(cola)