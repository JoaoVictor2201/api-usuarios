from flask import request, jsonify, Blueprint
from services.user_service import UserService

user_controller = Blueprint('user_controller', __name__, url_prefix='/users')
user_service = UserService()

@user_controller.route('/', methods=['GET'])
def get_usuarios():
    users = user_service.get_usuarios()
    return jsonify(users)

@user_controller.route('/<cpf>', methods=['GET'])
def get_usuario(cpf):
    user, message = user_service.get_usuario(cpf)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": message}), 404

@user_controller.route('/', methods=['POST'])
def create_usuario():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados inválidos"}), 400
    
    required_fields = ["nome", "email", "senha", "cpf"]
    for field in required_fields:
        if field not in data:
             return jsonify({"error": f"Campo {field} ausente"}), 400

    user, message = user_service.create_usuario(data['nome'], data['email'], data['senha'], data['cpf'])
    
    if user:
        return jsonify(user.to_dict()), 201
    else:
        return jsonify({"error": message}), 400

@user_controller.route('/<cpf>', methods=['DELETE'])
def delete_usuario(cpf):
    user, message = user_service.delete_usuario(cpf)
    if user:
        return jsonify({"message": message}), 200
    return jsonify({"error": message}), 404
