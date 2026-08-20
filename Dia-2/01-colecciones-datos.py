# Coleccion de datos es una variable que puede almacenar varios valores

#### Listas (List) ####
# ordenadas y que puede ser modificadas.
nombre = ['Pedro', 'Juan', 'Andres']
combinada = ['Edgar', 10, False, 12.5]

# siempren empiezan en la posicion cero.
print(nombre[0])

# cuando hacemos el uso de valores negativos en una lista internamente python le dara vuelta.
print(nombre[-1])

# si queremos ingresar a una posicion inexistente nos lanzara un error de 'indece fuera de rango'.
# print(nombre[10])

# pop() > remueve el ultimo elemento de la lista y se puede almacenar en otra variable
resultado = nombre.pop()
print(resultado)
print(nombre)

# append() > Ingresa un nuevo elemento a la ultima posicion de la lista
nombre.append('Luis')

# elimina el contenido de una posicion de la lista pero no lo podemos almacenar en otra variable.
del nombre[0]

# clear() > limpia toda la lista y la deja como nueva
nombre.clear()

# indicar una sub seleccion de la lista
print(combinada[1:4])

x = combinada[:]  # .copy()

# Copia la lista sin usar su misma posicion de memoria
print(combinada[:])

# desde la posicion inial hasta el 2
print(combinada[:2])

# desde posicion 2 hasta el final
print(combinada[2:])



meses_dscto = ['Enero', 'Marzo', 'Julio']
mes = 'Septiembre'

# not in > indicara si el valor no se encuentra en la lista
print(mes not in meses_dscto)

# in > indicara si el valor se encuentra en la lista
print(mes in meses_dscto)


# si sumamos las listas se combinaran
seccion_a=['pera','palta']
seccion_b=['aceite','atun']
print(seccion_a+seccion_b)

# ingrsar dato por el usuario
dato= input('Ingresar nombre')






#### Tuplas ####
# muy similar a la lista a excepcion que no se puede modificar. pero si se puede alterar sub colecciones como una lista.
# puede tener varios valores
cursos = ('backend','frontend')

mixto = (1,2,[5,6])
mixto[2][0] = 4

# para ver la cantidad de elementos de una tupla o lista
print(len(cursos))




#### Conjuntos (set) ####
# coleccion de datos DESORDENADA, una vez creada ya no se puede acceder a las posiciones de sus elementos
estaciones = {'verano','otoño','primavera','invierno'}

# de agrega de forma aleatoria
estaciones.add('otro')




#### Diccionarios ####
# una coleccion de datos desordenada pero ada elemento obedece a un llave definida
persona={
  'name': 'edgar',
  'lastname':'chavez'
}

# devuelve todas las llaves de mi dicionario
print(persona.keys())
# devuelve todos los contenidos de mi dicionario
print(persona.values())
# devuelve todas las llaves y su contenido en forma de tuplas dentro de una lista
print(persona.items())

# print(persona['name'])
# hacemos la busqueda de una llave y si no la encuentra nos retonara none
print(persona.get('names', 'No existe'))

# si definimos una llave que no existe, la creara, caso contrario modificara su valor
persona['age'] = 20
# NOTA: si la llave no es exactamente igual creara una nueva(tiene que coincidir minus y mayus)

# eliminar una llave de un diccionario
persona.pop('age')




