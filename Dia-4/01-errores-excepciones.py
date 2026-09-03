# Un error es una mala ejecucion del codigo que hara que mi proyecto o script deje de funcionar

# locals()['__builtins__'] > retornara del diccionario de locals()
# dir > lista los atributos como strings 
# locals() > devuelve todas las variables disponibles que tenemos en python en este scope
#print(dir(locals()['__builtins__']))

try:
  valor = int(input('Ingresa un numero: '))
  print(valor)
except TypeError:
  # entrara a este except cuando el error sea de tipo ValueError
  print('Error al convertir un string a un numero')
except Exception as error:
  # capturara el error causante impidiendo que el programa deje de funcionar
  print('Oops algo salio mal intentalo nuevamente')
  print(error.args) # argumentos del error



try:
  resultado = 1 / 0
except:
  print('Hubo un error')
else:
  # se ejecutara en caso no ingrese a un except
  print('Yo soy el else')
finally:
  print('S ejecutara si todo fue bien o mal')



# Example
productId = input('Ingresa el id del producto: ')
try:
  if(productId == '10'):
    # raise > emitira un error manualmente
    raise Exception('El producto no existe en la DB')
  # if validar la cantidad de productos
  # if validar la fecha de vencimiento
  print('La ejecucion continuara...')
except Exception as e:
  # ingresa si hubi un error
  print('Oops hubo un error', e.args[0])
else:
  # ingresa si NO hubo un error
  print('El prodcuto encontrado es: ...')
finally:
  # ingresa si hubo o no hubo error
  print({'message': 'Resultado final'})