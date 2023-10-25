from hashlib import sha256

from Common import CommonClass


class Auth(CommonClass):
    def __init__(self):
        super().__init__()
        self.auth = {
            'email': None,
            'password': None,
            'isAdmin': False,
            'isDelete': False,
        }
        self.authorize = {'isAuth': False, 'isLogin': False, 'user_id': None}

        self.getAuthUserQuery = "SELECT user_id, isAdmin,isDelete FROM auth WHERE email = %s and pass= %s"
        self.getAuthisDeleteQuery = "SELECT user_id, isDelete FROM auth WHERE email = %s and pass= %s"
        self.getAllAuthUserQuery = "SELECT id, user_id, email, isDelete FROM auth"
        self.getAllAuthUserDeleteQuery = "SELECT id, user_id, email, isDelete FROM auth WHERE isDelete = 1"

    def isTuplaEmpty(self, tupla):
        if len(tupla) == 0:
            return True
        else:
            return False

    def passModify(self, email, passwordOld, passwordNew):
        self.connectionDB.chagesPassAuthUser(email, sha256(passwordOld.encode(
            'utf-8')).hexdigest(), sha256(passwordNew.encode('utf-8')).hexdigest())

    def getAllAdmins(self):
        response_auth = self.connectionDB.sendQuery(
            self.getAllAuthUserAdminQuery)
        print(response_auth)

    def getAll(self):
        response_auth = self.connectionDB.sendQuery(self.getAllAuthUserQuery)
        print(response_auth)

    def isDelete(self, email, password):
        response_auth = self.connectionDB.sendQuery(
            self.getAuthisDeleteQuery, (email, sha256(password.encode('utf-8')).hexdigest()))
        if self.isTuplaEmpty(response_auth):
            return False
        else:
            return True

    def isAuthorized(self, email, password):
        response_auth = self.connectionDB.sendQuery(
            self.getAuthUserQuery, (email, sha256(password.encode('utf-8')).hexdigest()))
        if self.isTuplaEmpty(response_auth):
            return self.authorize
        else:
            user_id, isAdmin, isDelete = response_auth[0]
            if isDelete == 0 and isAdmin == 1:
                self.authorize['isAuth'] = True
                self.authorize['isLogin'] = True
                self.authorize['user_id'] = user_id
            elif isDelete == 0 and isAdmin == 0:
                self.authorize['isLogin'] = True
                self.authorize['user_id'] = user_id
            else:
                return self.authorize

    def deleteAuthUser(self, email, password):
        self.connectionDB.chagesIsDeleteAuthUser(
            1, email, sha256(password.encode('utf-8')).hexdigest())


# a = Auth()
# print(a.isAuthorize('roger@roge.com','password123456'))
