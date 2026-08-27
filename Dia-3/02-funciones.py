# Funciones 
# almacenara un bloque de codigo  con su compartamiento y solamente se ejecutara cuando este sea invocado(llamado)

def sumar(num1, num2):
  '''Funcion que recibe dos parametros'''
  print('se realizara la sumatoria')
  print(num1 + num2)


sumar(5, 7)


# mostrara la documentacion de la funcion si es que hay
print(sumar.__doc__)




usuario = []
# Funciones que retornan una respuerta
def registrar(nombre, email, telefono):
  usuario.append({
    'nombre': nombre,
    'email': email,
    'telefono': telefono
  })

  return {
    'message': 'Usuario regitrado exitosamente',
    'usuario': usuario[0]
  },1 , True
# si un funcion retorna mas de un valor (retornara una tupla) entonces podemos hacer dos cosas: 
# 1.- si solamente declararamos una sola variable ahi se almacenara toda la tupla.
# 2.- si queremos almacenar cada valor de la tupla en una variable podemos hacer una destructuracion de de esa tupla declarando el mismo numero de variables que el numero dr contenidos de la tupla
resultado, numero, booleano = registrar('Eduardo','ezed@gmail.com','988515582')
print(resultado)
print(numero)
print(booleano)



productos=[]
# parametros opcional siempre deben ir al final, primero los requeridos y luego los opcionales
def registrar_productos(nombre, precio, estado=True, almacen='cerrado'):
  productos.append({
    'nombre': nombre,
    'precio': precio,
    'estado': estado,
    'almacen': almacen
  })
  return 'Producto agregado exitosamente'

registrar_productos('tomate', 3.50)
registrar_productos('Manzana', 3.90)
registrar_productos('cebolla', 5.30, True, 'Almacen nuevo mercado')
# otra forma de pasar parametros
registrar_productos(almacen='Almacen rinconada', nombre='Pescado', precio=5)


# Numero indeterminado de parametros y lo almacenara en una tupla
# pueden ser diferentes tipos
# tambien se puede crear parametros normales, pero al final siempre va el generico (el que recibira n cantidad de parametros)
def alumnos(clase, *args):
  print(args)
alumnos('Backend','Maria','Jose','Pedro')

# kwargs > keyword argument
# si queremos recibir un numero ilimitado de argumentos pero estos deben de tener su nombre de parametro con su valor entonces usaremos kwargs y se alamacenaran en un diccionario
def ingresarProducto(**kwargs):
  print(kwargs)
  if(kwargs.get('nombre')):
    print('El usuario quiere agregar un producto con el nombre')
  if(kwargs.get('cantidad')):
    print('El usuario quiere ingresar la cantidad del produto')

ingresarProducto(nombre='Manzana', precio=3.20, estado=True, pais='Peru')
ingresarProducto(tamanio='grande', cantidad=100, nombre='pera de agua')





# Recusrsividad
# es utilizar la funcion dentro d la misma funcion
def saludar_n_veces(limite):
  if(limite == 0):
    return 'llege al limite'
  print('saludar')
  return saludar_n_veces(limite-1)
resultado = saludar_n_veces(10)

print(resultado)

# 5!  =  5 * 4 * 3 * 2 * 1  = 120
def factorial(limite):
  if limite == 0:
    return 1
  return limite * factorial(limite-1)
resultado = factorial(5)

print(resultado)


# Operador ternario
nombre, origen = 'Maria', 'Cuzco'
resultado = 'Me caso' if nombre == 'Maria' and origen == 'Arequipa' else 'Next'

# lambda function
# son funciones que pueden tener un numero indeterminado de argumentos pero solamente una expresion(na sola linea de ejecucion de codigo) ademas esta sera retornada.
cuadrado = lambda numero: numero ** 2
cuadrado(4)