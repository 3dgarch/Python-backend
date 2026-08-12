# Esto es un comentario

edad = 30

# Variables de texto
# Python no se puede crear una variable sin contenido
nombre = 'Ezed'
apellido = "De ' Casa"

# Saltos de linea
descripcion = """ Hola:
Peru
"""

descripcion2 = '''Hola:
Lima
'''

print(descripcion)

# Variables numericas
year = 2026
# type() => mostrara el tipo de variable
print(type(year))

# Variables en una sola linea
nombre, apellido, edad = 'Ezed', 'De Casa', 30


# None = null | undefined
name = None


# Ubicacion de memoria
print(id(edad))

# Eliminar variable de la memoria
del year

# Concatenar vario valores
print(nombre + " " + apellido + " " + str(edad))

# Metodo format
print("Mi nombre es {} {} y tengo {} años".format(nombre, apellido, edad))
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")

print("{1} tienes {0} años".format(edad, nombre))

