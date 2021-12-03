from flask import Flask, jsonify, request

#inicializar
app = Flask(__name__)

#importando archivo
from productos import productos

#prueba de conexion
@app.route('/ping')

def ping():
    return jsonify({"mensaje": "ping"})


#ruta GET
@app.route('/productos')

def prod():
    return jsonify({"productos": productos, "mensaje": "lista de productos"})

#ruta peticion GET por nombre de productos
@app.route('/productos/<string:productos_name>')

def getprod(productos_name):
    busqueda = [x for x in productos if x['name'] == productos_name]
    if (len(busqueda) > 0):
        return jsonify({"productos": busqueda[0]})
    return jsonify({"mensaje": "producto no encontrado"})

#ruta peticion POST (agregar)
@app.route('/productos', methods=['POST'])

def agregar():
    nuevo_prod = {
        "name": request.json["name"],
        "precio": request.json["precio"],
        "cantidad": request.json["cantidad"]
    }
    productos.append(nuevo_prod)
    return jsonify({"mensaje": "producto agregado satisfactoriamente", "productos": productos})


#ruta peticion PUT (modificar)
@app.route('/productos/<string:productos_name>', methods=['PUT'])

def modificar(productos_name):
    productos_mod = [x for x in productos if x["name"] == productos_name]
    if (len(productos_mod)> 0):
        productos_mod[0]["name"] = request.json["name"]
        productos_mod[0]["precio"] = request.json["precio"]
        productos_mod[0]["cantidad"] = request.json["cantidad"]
        return jsonify({
            "mensaje": "producto actualizado",
            "productos": productos
        })
        
        
#ruta peticion DELETE (eliminar)
@app.route('/productos/<string:productos_name>', methods=['DELETE'])

def eliminar(productos_name):
    eliminar = [x for x in productos if x["name"] == productos_name]
    if (len(eliminar) > 0):
        productos.remove(eliminar[0])
        return jsonify({
            "mensaje": "producto eliminado",
            "productos": productos
        })
    return jsonify({"mensaje": "producto no encontrado"})







if __name__ == '__main__':
    app.run(debug=True, port = 4000)
    