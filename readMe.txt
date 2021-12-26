- Tuplas
	Inmutables(no se pueden editar)
	funcion len() --- longitud
	método .index --- buscar
	método .count --- contar
	método .append --- añadir
- Conjuntos
	Desordenados
	conjunto = set()
	van entre {
	método .add --- añadir
	pertenencia a grupos con in
	Auto-eliminación de elementos duplicados
	cast de lista a conjunto y viceversa ---- lista=list(set(lista))
	cast de cadena a conjunto ---- cadena="esto es una cadena" set(cadena)
	

- Diccionarios
	diccionario = {}
	estructura: clave:valor
	añadir elementos: diccionario["clave"]="valor"
	función del() ---- eliminar una clave
	método .items() ---- nos facilita la lectura en clave y valor
	utilización de diccionarios y listas a la vez


- Pilas con listas (stacks)
	ultimo en entrar primero en salir
	.append
	.pop ---- sacar el último elemento
		

- Colas con listas (deque)
	primer elemento en entrar primero en salir
	debemos improtar la colección deque (from collections import deque)
	.append
	.popleft --- sacar un elemento de la cola



type() ---- tipo de una variable