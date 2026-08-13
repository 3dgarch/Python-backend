# Operadores de comparacion
num1, num2 = 10, 20

# Igual que
print(num1 == num2)

# Mayor que | Mayor igual que
print(num1 > num2)
print(num1 >= num2)

# Menor que | Menor igual que
print(num1 < num2)
print(num1 <= num2)

# Diferente de
print( num1 != num2)


# Operadore logicos
# Sirve para comparar varias comparaciones
# se utiliza and y or
print((10 > 5) and (10 < 20))
print((10 > 5) or (10 > 20))


# Operadores de identidad
# is
# is not
# sirve para ver si estan apuntando a la misma direccion de memoria
verduras = ['tomate','brocoli','zapallo']
verduras2 = verduras

verduras3 = ['tomate','brocoli','zapallo'] #['apio','cebolla','pepino']

print(verduras2 is verduras)

# NOTA: las colecciones de datos son variables nutables (cuando cambio su contenido este se vera reflejado en todas las copias de dicha variable)
verduras2[0] = 'peregil'

# El metodo copy() lo que hace es copia todo el contenido de la variable pero se guarda en una nueva posicion de memoria
verduras3 = verduras.copy()


# So hablamos de variables primitivas (str, int, floar, boolean, data) entonces al hacer la copia compartira  su mismo espacio de memoria PERO al hacer alguna modificacion a cuelaquiera de las dos o mas variable que esten usando el mismo espacio de memoria automaticamente python le asignara uno nuevo