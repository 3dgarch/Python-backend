nombre = 'Eduardo'


# si definimos una variable de manera global pero la queremos modificar dentro de una funcion no ser posible ya que al momento de querer modificarla nos pedira que esa variable exista de manera aislada dentro de esa funcion
def saludar():
  # global  > le indicamos a la funcion que utilizaremos una variable definida fuera de la misma para hacer modificaciones dentro de la funcion
  global nombre
  
  nombre = nombre * 2
  print(nombre)

saludar()
print(nombre)


# variable local
# solamente podran ser usadas dentro de las mismas
def example():
  ganacia = 0.15

example()