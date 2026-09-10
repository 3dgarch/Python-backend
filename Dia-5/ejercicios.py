# 1.- Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y  que lo dibuje usando *, ejemplo:
# para evitar el salto de linea podemos usar end=''. print('hola', end='*')
# altura: 2
# ancho: 10
# resultado:
# **********
# **********
# dibujar_rectangulo()
def dibujar_rectangulo():
  altura = int(input('Ingrese la altura del rectangulo: '))
  ancho = int(input('Ingrese el ancho del rectangulo: '))
  for i in range(altura):
    for j in range(ancho):
      print('*', end='')
    print()


# 2.- Ecriba una funcion que le ingresemos el grosor de un octogono y que lo dibuje usando *, ejemplo:
# dibujar_octogono()
def dibujar_octogono():
  grosor = int(input('Ingrese el grosor del octogono: '))
  for i in range(grosor):
    print(' ' * (grosor - i - 1) + '*' * (grosor + 2 * i) + ' ' * (grosor - i - 1))
  for i in range(grosor):
    print('*' * (grosor + 2 * grosor) + ' ' * (grosor - i - 1) + '*' * (grosor + 2 * grosor) + ' ' * (grosor - i - 1))
  for i in range(grosor):
    print(' ' * (i) + '*' * (grosor + 2 * (grosor - i - 1)) + ' ' * (i))


# 3.- ingresar un numero entero y debe llegar a 1 usando la serie de collatz.
# si el numero es par de divide entre 2
# si el numero es impar se multiplica por 3 y se le suma 1
# ejemplo 19
# 19 -> 58 -> 29 -> 88 -> 44 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# serie_collatz()
def serie_collatz():
  numero = int(input('Ingrese un numero entero: '))
  while numero != 1:
    print(numero, end=' -> ')
    if numero % 2 == 0:
      numero = numero // 2
    else:
      numero = numero * 3 + 1
  print(numero)
