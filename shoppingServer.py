from flask import Flask, jsonify, request, abort
from shoppinglistDAO import shoppinglistDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/shoppinglists')
def getAll():
    results = shoppinglistDAO.getAll()
    return jsonify(results)

@app.route('/shoppinglists/<int:id>')
def findById(id):
    foundshoppinglist = shoppinglistDAO.findByID(id)
    return jsonify(foundshoppinglist)

@app.route('/shoppinglists', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    shoppinglist = {
        "item": request.json['item'],
        "brand": request.json['brand'],
        "quantity": request.json['quantity']
    } 

    values=(shoppinglist['item'], shoppinglist['brand'], shoppinglist['quantity'])
    newId = shoppinglistDAO.create(values)
    shoppinglist['id'] = newId
    return jsonify(shoppinglist)

@app.route('/shoppinglists/<int:id>', methods=['PUT'])
def update(id):
    foundshoppinglist = shoppinglistDAO.findByID(id)
    if not foundshoppinglist:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json
    if 'quantity' in reqJson and type(reqJson['quantity']) is not int:
        abort(400)
    if 'item' in reqJson:
        foundshoppinglist['item'] = reqJson['item']
    if 'brand' in reqJson:
        foundshoppinglist['brand'] = reqJson['brand']
    if 'quantity' in reqJson:
        foundshoppinglist['quantity'] = reqJson['quantity']
    values = (foundshoppinglist['item'], foundshoppinglist['brand'], foundshoppinglist['quantity'], foundshoppinglist['id'])

    shoppinglistDAO.update(values)

    return jsonify(foundshoppinglist)

@app.route('/shoppinglists/<int:id>', methods=['DELETE'])
def delete(id):
    shoppinglistDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main' :
    app.run(debug=True)