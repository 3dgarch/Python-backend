# Prgramacion Orientada a  Objetos > POO | OOP
# la programacion debe estar creada en base a clases
# clases > son plantillas para que puedan se utilizadas varias veces sin lanecesidad de modificar su forma en relacion al abjeto sino que al revez.

class Persona:
  # las variables creadas dentro de la clase pasan  a llamarse atributos
  fec_nac = '1996-01-2'
  nombre = 'Fernanda'

  # las acciones que puede tener una clase se definen como funciones, pero una funcion al ser creada dentro de una clase pasa a llamarse metodo
  # siempre como primer parametro obligatoriamente se usa self para hacer referencia dentro de la instancia a los atributos y metodos
  def saludar(self):
    print('Hola {}'.format(self.nombre))

# cuando una variable se crea a raiz se una clase, esta variable pasa a llamar instancia (instancia > copia en su totalidad de la clase)
persona1 = Persona()


# un atributo estatico es un atributo que puede ser accedido sin la necesidad de crear una instancia 
# por defecto python cualquier atributo creado a nivel de la clase es un atributo estatico