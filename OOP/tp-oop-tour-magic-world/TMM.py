import getch
import pwinput

from Attraction import Attraction
from Auth import Auth
from Common import CommonClass
from Promotion import Promotion
from User import User


class SystemTMM(CommonClass):
    def __init__(self):
        super().__init__()
        self.continuar = True
        self.EMAIL = "Email: "
        self.PASSWORD = "Password: "
        self.PASSWORD_OLD = "Password anterior: "
        self.PASSWORD_NEW = "Password nueva: "
        self.AVAILABLE_TIME = "Ingresar tiempo disponible: "
        self.BUDGET = "Ingresar presupuesto: "
        self.USER_FULL_NAME = "Ingresar Nombre y Apellido: "
        self.TITULO_INITIAL = "MENÚ DE INICIAL"
        self.TITULO_LOGIN = "INICIO DE SESIÓN"
        self.TITULO_USER = "MENÚ DE USUARIO"
        self.TITULO_USER_ADMIN = "MENÚ DE USUARIO ADMIN"
        self.TITULO_REGISTER_USER = "MENÚ DE REGISTRO DE USUARIO"
        self.TITULO_REFILL_USER = "RECARGA DE DINERO Y DISPONIVILIDAD DE USUARIO"
        self.TITULO_PROMOTION = "MENÚ DE PROMOCIONES"
        self.TITULO_ATTRACTION = "MENÚ DE ATRACCIONES"
        self.TITULO_USER_PROMOTION_ATTRACTION = "MENÚ SUGERENCIAS DE PROMOCIONES Y ATRACCIONES"
        self.TITULO_USER_PROMOTION_ATTRACTION_END = "TUS PROMOCIONES O ATRACCIONES"
        self.CATEGORIAS = ["AVENTURA", "DEGUSTACION", "PAISAJE"]
        self.MESSAGE_INITIAL = "Presione cualquier tecla para continuar o Esc para finalizar"
        self.promotion = Promotion()
        self.auth = Auth()
        self.user = User()
        self.attraction = Attraction()
        self.user_time_disponivility = 0
        self.user_budget_current = 0
        self.MESSAGE_USER_PROMOTION_ATTRACTION = "Cuentas con un presupuesto: ${} y una disponibilidad: {}hs"
        self.MESSAGE_USER_PROMOTION_ATTRACTION_EMTY = "Pero no es suficiente para disfrutar de nuestras astracciones, deberas disponer de mayor presupuesto y disponibilidad. \n Siendo redireccionado para cargar mas dinero y tiempo."
        self.INITIAL_OPCION = ["INGRESAR", "REGISTRASE", "SALIR"]
        self.OPCIONES_USER = ["MODIFICAR MIS DATOS PERSONALES", "CAMBIAR PASSWORD",
                              "MIS PROMOCIONES O ATRACCIONES", "SALIR AL INICIO"]
        self.OPCIONES_ADMIN = ["MODIFICAR USUARIO", "MODIFICAR PASSWORD" "BORRAR USUARIO", "VER TODOS LOS USUARIOS", "CREAR NUEVA PROMO",
                               "MODIFICAR PROMO", "BORRAR PROMO", "CREAR ATRACCION", "MODIFICAR ATRACCION", "BORRAR ATRACCION", "SALIR AL INICIO"]
        self.ERROR_MESSAGE_PROMOTION = "No tiene sufuciente dinero para más promosiones"
        self.INPUT = "Seleccione una de las opción (1-%s): "
        self.ERROR_OPTION_MESSAGE = "Este numero de opcion: %s no es correcto."
        self.ERROR_MESSAGE = "Debes escribir un numero valido."
        self.ERROR_MESSAGE_LOGIN = "Clave o Email invalido"
        self.ERROR_MESSAGE_USER = "No es Valido"
        self.MESSAGE_USER = "Usuario ya existe"
        self.MESSAGE_NEW_PASSWORD = "Recuerde su nueva password"
        self.listCosts = []
        self.attractions_user_category = None
        self.promotions_user_category = None
        self.userSelected = []
        self.filter = []

    def teclaEsc(self):
        print(self.MESSAGE_INITIAL)
        tecla = getch.getch()
        if tecla.lower() == chr(27):
            self.exitSystem()

    def menUsuario(self):
        self.title(self.TITULO_USER)
        self.options(self.OPCIONES_USER)
        opcion = int(input(self.INPUT % len(self.OPCIONES_USER)))
        if (opcion < 0) or (opcion > len(self.OPCIONES_USER)):
            print(self.ERROR_OPTION_MESSAGE % opcion)
        else:
            match opcion:
                case 1: self.setUser()
                case 2: self.changePass()
                case 3: self.promotionUser()
                case 4: self.menuInitial()

    def title(self, title):
        print(title)
        print("-" * len(title))

    def options(self, list):
        for index, option in enumerate(list):
            print(f'{index + 1}. {option}')

    def getUserData(self):
        nombreApellido = input(self.USER_FULL_NAME)
        try:
            categoria = ''
            self.options(self.CATEGORIAS)
            opcion = int(input(self.INPUT % len(self.CATEGORIAS)))
            if (opcion > 0) and (opcion > len(self.INITIAL_OPCION)):
                print(self.ERROR_OPTION_MESSAGE % opcion)
            else:
                match opcion:
                    case 1: categoria = 'AVENTURA'
                    case 2: categoria = 'DEGUSTACION'
                    case 3: categoria = 'PAISAJE'
        except ValueError:
            print(self.ERROR_MESSAGE)
        try:
            presupuesto = int(input(self.BUDGET))
            if (presupuesto < 0):
                print(self.ERROR_MESSAGE_USER)
        except ValueError:
            print(self.ERROR_MESSAGE)
        try:
            tiempoDisponible = int(
                input(self.AVAILABLE_TIME))
            if (tiempoDisponible < 0):
                print(self.ERROR_MESSAGE_USER)
        except ValueError:
            print(self.ERROR_MESSAGE)
        return (nombreApellido, categoria, presupuesto, tiempoDisponible)

    def menuInitial(self):
        self.title(self.TITULO_INITIAL)
        self.options(self.INITIAL_OPCION)
        opcion_initial = int(input(self.INPUT % len(self.INITIAL_OPCION)))
        if (opcion_initial < 1) or (opcion_initial > len(self.INITIAL_OPCION)):
            print(self.ERROR_OPTION_MESSAGE % opcion_initial)
        else:
            if opcion_initial == 1:
                self.login()
            elif opcion_initial == 2:
                self.register()
            elif opcion_initial == 3:
                self.exitSystem()

    def register(self):
        self.title(self.TITULO_REGISTER_USER)
        email = input(self.EMAIL).lower()
        password = input(self.PASSWORD)
        chekAuth = self.auth.isAuthorized(email, password)
        if self.auth.isDelete(email, password):
            self.connectionDB.chagesIsDeleteAuthUser(
                0, email, sha256(password.encode('utf-8')).hexdigest())
            print(self.MESSAGE_USER)
            self.salir_programa()
        elif chekAuth['isLogin']:
            print(self.MESSAGE_USER)
            self.salir_programa()
        else:
            nombreApellido, categoria, presupuesto, tiempoDisponible, = self.getUserData()
            self.user.createNewUser(
                nombreApellido, categoria, presupuesto, tiempoDisponible, email, password)
        self.login()

    def setUser(self):
        nombreApellido, categoria, presupuesto, tiempoDisponible, = self.getUserData()
        self.user.userModify(
            self.auth.authorize['user_id'], nombreApellido, categoria, presupuesto, tiempoDisponible)
        self.menUsuario()

    def changePass(self):
        email = input(self.EMAIL).lower()
        passwordOld = pwinput.pwinput(prompt=self.PASSWORD_OLD)
        print(self.MESSAGE_NEW_PASSWORD)
        passwordNew = input(self.PASSWORD_NEW)
        self.auth.passModify(email, passwordOld, passwordNew)
        self.menUsuario()

    def sort_by_cost_descending(self, element):
        return element['total_cost']

    def fillBudgetTime(self):
        self.title(self.TITULO_REFILL_USER)
        try:
            presupuesto = int(input(self.BUDGET))
            if (presupuesto < 0):
                print(self.ERROR_MESSAGE_USER)
        except ValueError:
            print(self.ERROR_MESSAGE)

        try:
            tiempoDisponible = int(
                input(self.AVAILABLE_TIME))
            if (tiempoDisponible < 0):
                print(self.ERROR_MESSAGE_USER)
        except ValueError:
            print(self.ERROR_MESSAGE)

        self.user.userRefill(self.auth.authorize['user_id'], {
                             'presupuesto': presupuesto, 'tiempoDisponible': tiempoDisponible})
        self.menUsuario()

    def showSelected(self):
        print()
        print(self.MESSAGE_USER_PROMOTION_ATTRACTION.format(
            self.user_budget_current, self.user_time_disponivility))
        print()
        if not self.userSelected:
            print(self.MESSAGE_USER_PROMOTION_ATTRACTION_EMTY)
            self.fillBudgetTime()
        else:
            self.title(self.TITULO_USER_PROMOTION_ATTRACTION_END)
            for index, option in enumerate(sorted(self.userSelected, key=self.sort_by_cost_descending, reverse=True)):
                print(f'{index + 1}. {option["name"]}')
            self.menUsuario()

    def find_uncompared_attractions(self):
        selected_attractions = set()
        for pack in self.userSelected:
            selected_attractions.update(pack.get("attractions_compared", []))
        filtered_data = [
            item for item in self.listCosts if "attractions_compared" not in item or item["name"] not in selected_attractions]
        filtered = [
            item for item in filtered_data if "attractions_compared" in item and item["name"] not in selected_attractions]
        newFilter = []
        for item in filtered:
            if item["total_duration"] <= int(self.user_time_disponivility) and item["total_cost"] <= self.user_budget_current:
                newFilter.append(item)

        if not newFilter:
            self.showSelected()
        else:
            self.filter = newFilter

    def menuPromotionsAttraction(self):
        self.find_uncompared_attractions()
        print()
        print(self.MESSAGE_USER_PROMOTION_ATTRACTION.format(
            self.user_budget_current, self.user_time_disponivility))
        print()
        self.title(self.TITULO_USER_PROMOTION_ATTRACTION)
        print(f'0. Exit')
        for index, option in enumerate(sorted(self.filter, key=self.sort_by_cost_descending, reverse=True)):
            print(f'{index + 1}. {option["name"]}')
        opcion = int(
            input(f"Select an option (0-{len(self.filter)+1}): "))
        if opcion == 0:
            self.menUsuario()
        if 1 <= opcion <= len(self.filter):
            selected_option = self.filter[
                opcion - 1]
            self.userSelected.append(selected_option)
            self.listCosts.remove(selected_option)
            self.user_time_disponivility -= selected_option['total_duration']
            if selected_option['total_cost_discount'] != 'none':
                self.user_budget_current -= selected_option['total_cost_discount']
                self.menuPromotionsAttraction()
            else:
                self.user_budget_current -= selected_option['total_cost']
                self.menuPromotionsAttraction()
        else:
            print(f"Invalid option: {opcion}")

    def promotionUser(self):
        print('calculando prmo...')
        self.listCosts = []
        user_response = self.user.getUserById(self.auth.authorize['user_id'])
        self.user_time_disponivility = round(float(user_response[3]), 2)
        self.user_budget_current = user_response[2]
        favorite_user_category = user_response[1]
        self.promotions_user_category = self.promotion.getPromotionByCatergory(
            favorite_user_category)
        self.attractions_user_category = self.attraction.getAttractionByCategoryType(
            favorite_user_category)
        for tuplaPromotion in self.promotions_user_category:
            totalCost = []
            totalDuration = []
            attractionsCompared = []
            attractionsCompared.append(tuplaPromotion[4])
            if (tuplaPromotion[5] != 'Null' and tuplaPromotion[5] != None):
                attractionsCompared.append(tuplaPromotion[5])
            elif (tuplaPromotion[6] != 'Null' and tuplaPromotion[6] != None):
                attractionsCompared.append(tuplaPromotion[6])
            for tuplaAttraction in self.attractions_user_category:
                if tuplaAttraction[1] == tuplaPromotion[4] or tuplaAttraction[1] == tuplaPromotion[5] or tuplaAttraction[1] == tuplaPromotion[6]:
                    totalCost.append(tuplaAttraction[2])
                    totalDuration.append(tuplaAttraction[3])
            if (self.user_time_disponivility >= sum(totalDuration) and self.user_budget_current >= self.promotion.discount(sum(totalCost), tuplaPromotion[1], tuplaPromotion[7])):
                self.listCosts.append(
                    {'id_promotion': tuplaPromotion[0], 'name': tuplaPromotion[2], 'total_cost': self.promotion.discount(sum(totalCost), tuplaPromotion[1], tuplaPromotion[7]), 'total_duration': sum(totalDuration), "attractions_compared": attractionsCompared})
        for tuplaAttraction in self.attractions_user_category:
            if (self.user_time_disponivility >= tuplaAttraction[3] and self.user_budget_current >= tuplaAttraction[2]):
                self.listCosts.append(
                    {'id_attraction': tuplaAttraction[0], 'name': tuplaAttraction[1], 'total_cost_discount': 'none', "total_cost": tuplaAttraction[2], 'total_duration': tuplaAttraction[3], "attractions_compared": [tuplaAttraction[1]]})
        print(self.listCosts)
        if not self.listCosts:
            self.showSelected()
        else:
            self.menuPromotionsAttraction()

    def menuAdmin(self):
        self.title(self.TITULO_USER_ADMIN)
        self.options(self.OPCIONES_ADMIN)
        opcion = int(input(self.INPUT_ADMIN % len(self.OPCIONES_ADMIN)))
        if (opcion < 0) or (opcion > len(self.OPCIONES_ADMIN)):
            print(self.ERROR_OPTION_MESSAGE % opcion)
        else:
            match opcion:
                case 1: print("Seleccione 1")
                case 2: print("Seleccione 2")
                case 3: print("Seleccione 3")
                case 4: print("Seleccione 4")
                case 5: print("Seleccione 4")
                case 6: print("Seleccione 4")
                case 7: print("Seleccione 4")
                case 8: print("Seleccione 4")
                case 9: print("Seleccione 4")
                case 10: print("Seleccione 4")
                case 11: self.menuInitial()

    def login(self):
        self.title(self.TITULO_LOGIN)
        # email = input(self.EMAIL).lower()
        # password = pwinput.pwinput(prompt=self.PASSWORD)
        print()
        # self.auth.isAuthorized(email, password)
        self.auth.isAuthorized('ron@ron.com', '98765')
        if self.auth.authorize['isAuth'] and self.auth.authorize['isLogin']:
            self.menuAdmin()
        elif self.auth.authorize['isLogin']:
            self.menUsuario()
        else:
            print(self.ERROR_MESSAGE_LOGIN)

    def main(self):
        while self.continuar:
            self.teclaEsc()
            self.menuInitial()

    def exitSystem(self):
        self.greeting()
        self.salir_programa()


if __name__ == "__main__":
    programa = SystemTMM()
    programa.main()
