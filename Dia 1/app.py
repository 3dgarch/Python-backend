from flask import Flask, request
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

# si solamente mandamos a llamar  a la clase y le pasamos la instancia de la clase Flask creara los permisos para que todos puedan acceder (Allowed-Origin), para que cualquier metodo pueda ser consultado (All-Method) y para cualquier header (All-Header).
# origin > '*' indica que origenes pueden consumir mi API
# methos > ['GET','POST','PUT','DELETE','PATCH']
# allow-headers > 
CORS(app=app, origins='http://127.0.0.1:5500', methods=['*'], allow_headers=['Content-Type'])

clientes = [
    {
        "name": "Eduardo",
        "contry": "PERU",
        "age": "30",
        "id": 1,
    },
    {
        "name": "Maria",
        "contry": "PERU",
        "age": "40",
        "id": 2,
    }
]


def buscar_cliente(id):
    #resultado = None
    # iterar la lista y buscaremos el clilente por ese id y si no existe imprimir un mensaje.
    # for cliente in clientes:
    #     if cliente.get('id') == id:
    #         return cliente

    for posicion in range(0, len(clientes)):
        cliente = clientes[posicion]
        if clientes[posicion].get("id") == id:
            return (cliente, posicion)         # ({}, int)


@app.route("/")
def estado():
    hora_del_servidor = datetime.now()
    return {"status": True, "hour": hora_del_servidor.strftime("%H:%M:%S")}


@app.route("/clientes", methods=["POST", "GET"])
def obtener_clientes():
    # Solamente puede ser llamado en cada controlador (funcion que se ejecutara cuando se realice una peticion desde el cliente)
    print(request.method)  # mostrar el metodo de la peticion
    
    print(request.data)  # mostrar el contenido de la peticion en bytes

    # print(
    #     request.get_json()
    # )  # mostrar el contenido de la peticion en formato json

    if request.method == "POST":
        # ingresara cuando sea post
        data = request.get_json()
        # data > agregar una llave llamada id que sera la longuitud de la lista actual
        data["id"] = len(clientes) + 1
        clientes.append(data)
        return {"message": "Cliente agregado exitosamente", "client": data}
    elif request.method == "GET":
        # ingresara cuando sea GET
        return {"message": "Lista de clientes", "clients": clientes}


@app.route("/cliente/<int:id>", methods=["GET", "PUT", 'DELETE'])
def gestion_usuario(id):

    if request.method == "GET":
        resultado = buscar_cliente(id) # resultado > ({}, int)
        if resultado:
            return resultado[0] # {}
        else:
            return {"message": "El susuario a buscar no se encontro"}
        
    elif request.method == "PUT":
        resultado = buscar_cliente(id)  # 'resultado' es una tupla: (dict_cliente, int_posicion)
        if resultado:
            # resultado[0] -> Diccionario del cliente
            # resultado[1] -> Índice o posición del cliente en la lista

            # Extraemos la información en formato JSON enviada en el body de la petición
            data = request.get_json()

            # Aseguramos/Forzamos que el objeto mantenga el ID correspondiente a la URL
            data['id'] = id

            # Extraemos la posición exacta del cliente dentro de la lista
            posicion = resultado[1]

            # Reemplazamos el cliente antiguo por el nuevo objeto en la lista
            clientes[posicion] = data

            # Retornamos el objeto actualizado (Flask responderá con HTTP 200 por defecto)
            return data
        else:
            return {"message": "El usuario a modificar no se encontró"}, 404

    elif request.method == 'DELETE':
        resultado = buscar_cliente(id)

        if resultado:
            [cliente, posicion] = resultado
            cliente_Eleminado = clientes.pop(posicion)
            return {
                'message': 'Cliente eliminado exitosamente',
                'cliente': cliente_Eleminado
            }
        else: 
            return {'message': 'El cliente a elminar no se encontro'}, 404

# Reiniciar el servidor cada vez que se realicen cambios en el código(True)
app.run(debug=True)
