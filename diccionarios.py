
animales = {"caballo":"", "vaca":""} #Los diccionarios van entre {}
print(type(animales)) #Con el metodo type sabemos el tipo de una variable
 

animales["perro"] = "dog"
animales["gato"] = "cat"
animales["rana"] = "frog"
 
animales["caballo"] = "horse"
animales["vaca"] = "cow"
 
del(animales["rana"])
del(animales["vaca"])
