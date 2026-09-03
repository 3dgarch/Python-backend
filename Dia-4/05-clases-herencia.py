# herencia > extraer informacion de una clase padre

class Usuario:
  def __init__(self, nombre, apellido, correo):
    self.nombre = nombre
    self.apellido = apellido
    self.correo = correo
  def saludar(self):
    return 'Hola soy {}'.format(self.nombre)

# alumno  ha heredado todos los atributos y metodos  de la clase padre (Usuario)
class Alumno(Usuario):
  def __init__(self, nombre, apellido, correo, curso):
    # super() > sirve para llamar a la clase de la cual estamos haciendo la herencia para no volver a escribir las misma logica
    super().__init__(nombre, apellido, correo)
    self.curso = curso
  def info(self):
    return {
      'nombre': self.nombre,
      'apellido': self.apellido,
      'correo': self.correo,
      # 'saludar': self.saludar()
      'saludar': super().saludar()
    }

alumnoPedro = Alumno('Pedro', 'Flores', 'pedro@gmail.com', 'Backend')