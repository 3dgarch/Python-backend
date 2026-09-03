# encapsulamiento > se declara tipos de accesibilidad a los atributos y metodos
class Producto:
  def __init__(self, nombre, precio):
    # existen 3 tipos de accesibilidad a los atributos y metodos de una clase: 
    # public
    self.nombre = nombre
    self.precio = precio

    # privado : cuando se define un atributo  don '__' estaremos indicando que esta sera privado y no podra sera accedida desde afuera de la clase ni de su misma instancia
    self.__ganancia = self.precio * 0.30

    # protegido protected
  def mostrar_info(self):
    return {
      'nombre': self.nombre,
      'precio': self.precio,
      # {:.2f} indicamos que convertiremos este valor  a string  y solamente lo limtaremos a tenes 2 decimales
      'igv': '{:.2f}'.format(self.__calcular_igv())
    }
  def __calcular_igv(self):
    resultado = self.precio * 0.18
    return resultado

taza = Producto('taza', 10)

# atributo publico = porque puedo acceder a este tanto desde la misma clase como en su instancia
taza.nombre

# atributo privado = solamente podra ser accedido a el dentro de la misma clase pero no desde su instancia
# taza.__ganancia   # esto dara error
