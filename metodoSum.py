#Programa para sumar todos los numeros pares entre el 0 hasta el 100:

print("Comienzo a sumar...")

suma=sum(range(0,101,2))
print("La suma de todos los números pares es: ",suma)

#Con bucle while
numero=0
suma=0
while numero<=100:
    if numero%2==0:
        suma+=numero
    numero+=1
print("la suma de todos los números es: ",suma)