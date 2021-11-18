from flask import Flask, jsonify, request, abort
from bookDAO import bookDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/books')
def getAll():
    results = bookDAO.getAll()
    return jsonify(results)

@app.route('/books/<int:id>')
def findById(id):
    foundBook = bookDAO.findByID(id)
    return jsonify(foundBook)

@app.route('/books', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    book = {
        "Title": request.json['Title'],
        "Author": request.json['Author'],
        "Price": request.json['Price']
    } 

    values=(book['Title'], book['Author'], book['Price'])
    newId = bookDAO.create(values)
    book['id'] = newId
    return jsonify(book)

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundbook = bookDAO.findByID(id)
    if not foundbook:
        abort(404)

    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)
    if 'Title' in reqJson:
        foundbook['Title'] = reqJson['Title']
    if 'Author' in reqJson:
        foundbook['Author'] = reqJson['Author']
    if 'Price' in reqJson:
        foundbook['Price'] = reqJson['Price']
    values = (foundbook['Title'], foundbook['Author'], foundbook['Price'], foundbook['id'])

    bookDAO.update(values)

    return jsonify(foundbook)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    bookDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main' :
    app.run(debug=True)