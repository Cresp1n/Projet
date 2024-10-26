from flask import Flask, jsonify, request

# Initialiser l'application Flask
app = Flask(__name__)

# Exemple de données en mémoire
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

# Route pour récupérer tous les éléments
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Route pour récupérer un élément par ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404

# Route pour ajouter un nouvel élément
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Route pour mettre à jour un élément existant
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        updated_data = request.get_json()
        item.update(updated_data)
        return jsonify(item)
    else:
        return jsonify({"message": "Item not found"}), 404

# Route pour supprimer un élément
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
