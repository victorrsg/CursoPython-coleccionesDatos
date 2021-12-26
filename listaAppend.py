#lista.append ----> añadir un item a la lista

lista1=["h","o","l","a","m"]
lista2=["h","o","l","a","m","a","r"]

lista3=[]
for letra in lista1:
    if letra in lista2 and letra not in lista3:
        lista3.append(letra)

print(lista3)