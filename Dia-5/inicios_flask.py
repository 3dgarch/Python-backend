# No se puede crear un archivo con el mismo nombre de una libreria que vamos a utilizar
from flask import Flask
from datetime import datetime

# instancia de la clase Flask
# __name__ mostrara si el archivo es el archivo raiz o principal del proyecto y si lo es entonces el valor de __name__ sera igual a __main__
app = Flask(__name__)

# los decoradores es un patron de diseño que nos permite modificar el comportamiento de una funcion sin modificar su codigo fuente, es decir, podemos agregarle funcionalidades a una funcion sin modificar su codigo fuente
@app.route('/')
def inicial():
  print('Hola mundo')
  # siempre en los controladores de flask debemos retornar una respuesta, ya sea un string, un diccionario o un objeto json
  return 'Bienvenido a mi primer servidor web con flask'

@app.route('/api/info')
def info_app():
  return {
    'nombre': 'Mi primer servidor web con flask',
    'version': '1.0.0',
    'fecha': datetime.now()
  }



# inicializamos el servidor web
app.run(debug=True) # debug=True nos permite ver los errores en la consola y reiniciar el servidor automaticamente cuando hacemos cambios en el codigo fuente