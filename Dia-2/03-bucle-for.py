notas = [10, 20, 13]
for nota in notas:
  print(nota)

# bucle para iteracion hasta el limite definido
# si ponemos tres parametros el primero indicara el numero inicial. El segundo el tope y el tercero sera de cuanto en cuanto hara la incrementacion o decrementacion.

for numero in range(5, 20, 2): # empezara en 5, hasta <10 y en cada ciclo incrementara en 2 unidades
  print(numero)

for posicion in range(3):
  print(notas[posicion])

aprobados =[]
for aprobado in aprobados:
  print(aprobado)
# el else en el caso de los for se ejecutara despues de haber hecho la iteracion del bucle FOR
# el else se ejecutara si el for termino sin problemas
else: 
  print('Ya no hay mas aprobados')



productos = ['manzana', 'pera','tallarines','tazas']

busqueda = input('Ingrese el producto a buscar')
for producto in productos:
  if producto == busqueda:
    print('El producto si esta la tienda')
    break
# el else se colocara si al finalizar no hubo un brak osea todo finalizo sin una busqueda esperada
else:
  print('no se encontro el producto')