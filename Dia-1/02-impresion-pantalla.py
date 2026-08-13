# Variables en una sola linea
nombre, apellido, edad = 'Ezed', 'De Casa', 30

# Concatenar vario valores
print(nombre + " " + apellido + " " + str(edad))

# Metodo format
print("Mi nombre es {} {} y tengo {} años".format(nombre, apellido, edad))
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")

print("{1} tienes {0} años".format(edad, nombre))