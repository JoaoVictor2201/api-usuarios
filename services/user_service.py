from models.user_model import User

class UserService:
    def __init__(self):
        self.users = []

    def create_usuario(self, name, email, password, cpf):
        user, _ = self.get_usuario(cpf)
        if user:
            return None, "Usuário já existe"
        
        new_user = User(name, email, password, cpf)
        self.users.append(new_user)
        return new_user, "Usuário criado com sucesso"

    def get_usuarios(self):
        return [user.to_dict() for user in self.users]

    def get_usuario(self, cpf):
        for user in self.users:
            if user.cpf == cpf:
                return user, None
        return None, "Usuário não encontrado"

    def delete_usuario(self, cpf):
        user, _ = self.get_usuario(cpf)
        if user:
            self.users.remove(user)
            return True, "Usuário deletado com sucesso"
        return False, "Usuário não encontrado"
