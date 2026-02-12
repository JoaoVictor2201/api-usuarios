class User:
    def __init__(self, name, email, password, cpf):
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf

    def to_dict(self):
        return {
            "nome": self.name,
            "email": self.email,
            "senha": self.password,
            "cpf": self.cpf
        }
