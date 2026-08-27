# Mientras que
numero = 0


while numero < 10:
  # pass > sirve para indicar dentro de un bloque de codigo que aun no hemos definido la logica
  pass

  # bucle infinito (infinite loop) > es un ciclo que se va a ejecutar por siempre y nunca trndra fin
  numero += 1
else:
  print('el while termino bien')


# en relacion a los siguientes numeros indicar cuantos son pares y cuanto son impares
numeros = [1, 5, 16, 28, 234, 67, 29]


posicion = 0
par, impar  = 0, 0

while posicion < len(numeros):
  if numeros[posicion] % 2 == 0:
    par += 1
  else: 
    impar += 1
  posicion += 1






for numero in numeros:
  if numero % 2 == 0:
    par += 1
  else: 
    impar += 1

print('Hay {} numeros pares'. format(par))
print('Hay {} numeros impares'.format(impar))



