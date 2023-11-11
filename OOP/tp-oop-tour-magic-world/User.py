import datetime
from hashlib import sha256

from Common import CommonClass


class User(CommonClass):
    def __init__(self):
        super().__init__()
        self.current = datetime.datetime.now()
        self.user = {
            'nombreApellido': None,
            'categoria': None,
            'presupuesto': 0,
            'tiempoDisponible': 24.00,
            'timestamp': None,
        }
        self.is_delete = False
        self.userById = "SELECT nombre_apellido, categoria, presupuesto, tiempo_disponible FROM usuarios WHERE id = %s"

    def getUserById(self, id_user):
        response_user = self.connectionDB.sendQuery(
            self.userById, (id_user))
        for result in response_user:
            return result

    def createNewUser(self, nombreApellido, categoria, presupuesto, tiempoDisponible, email, password):
        self.user['nombreApellido'] = nombreApellido
        self.user['categoria'] = categoria
        self.user['presupuesto'] = presupuesto
        self.user['tiempoDisponible'] = tiempoDisponible
        self.user['timestamp'] = self.current.timestamp()

        self.connectionDB.addNewUser(self.user, email, sha256(
            password.encode('utf-8')).hexdigest())

    def userModify(self, user_id, nombreApellido, categoria, presupuesto, tiempoDisponible):
        self.user['nombreApellido'] = nombreApellido
        self.user['categoria'] = categoria
        self.user['presupuesto'] = presupuesto
        self.user['tiempoDisponible'] = tiempoDisponible

        self.connectionDB.upDateUser(user_id, self.user)

    def userRefill(self, user_id, user):
        self.connectionDB.upDateUserBudgetTime(user_id, user)

    def __repr__(self):
        return f'{self.user}'


# user = User()
# print(user.getUserById(14))
