class Animal:
  # metodo constructor: este metodo se llamara cuamdo vayamos a crear una nueva instancia de la clase
  def __init__(self, nombre, sexo):
    # crear nuevos atributos dentro de la clase y estos ya no seran staticos
    self.nombre = nombre
    self.sexo = sexo
  def description(self):
    return 'Yo soy un {}, y soy {}'.format(self.nombre, self.sexo)

perro = Animal('Drako','M')

print(perro.description())