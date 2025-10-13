from flask import Blueprint, request, jsonify
from src.services.item_service import ItemService

api = Blueprint('api', __name__)

@api.route('/items', methods=['POST'])
def create_item():
    result = ItemService.create_item(request.get_json())
    return jsonify(result.dict()), 201

@api.route('/items', methods=['GET'])
def get_items():
    items = ItemService.get_all_items()
    return jsonify([item.dict() for item in items])

@api.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = ItemService.get_item_by_id(item_id)
    return jsonify(item.dict())

@api.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = ItemService.update_item(item_id, request.get_json())
    return jsonify(item.dict())

@api.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    ItemService.delete_item(item_id)
    return jsonify({"message": "Item deleted successfully"})

