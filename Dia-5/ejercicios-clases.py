# crear una clase Persona en la cual se guarden su nombre, fecha_nacimiento. nacionalidad, dni, ademas tambien una clase Alumno y una clase Docente en la cual el alumno, a diferencia del docente, tenga una serie de cursos matariculados, y el  docente tenga un numero de seguro social y su cuenta de la cts, en base a lo visto de herencia codificar las clases y ademas ver si hay algun atributo o metodo que deba de ser privado.

class Persona:

  def __init__(self, nombre, fec_nacimiento, dni, nacionalidad="PERUANA"):
    # Al escribir 'self.nombre', Python CREA el atributo inmediatamente
    self.nombre = nombre
    self.fec_nacimiento = fec_nacimiento
    self.dni = dni
    self.nacionalidad = nacionalidad
  def saludar(self):
    print("Hola, me llamo {}".format(self.nombre))


class Alumno(Persona):
  def __init__(self, nombre, fec_nacimiento, dni, nacionalidad, cursos):
    super().__init__(nombre, fec_nacimiento, dni, nacionalidad)
    # Al escribir 'self.__cursos', Python CREA el atributo inmediatamente y lo hace privado, es decir, no se puede acceder desde fuera de la clase
    self.__cursos = cursos

class Docente(Persona):
  def __init__(self, nombre, fec_nacimiento, dni, nacionalidad, seguro_social, cts):
    super().__init__(nombre, fec_nacimiento, dni, nacionalidad)
    # self.__seguro_social atributo privados, es decir, no se puede acceder desde fuera de la clase
    self.__seguro_social = seguro_social
    self.cts = cts