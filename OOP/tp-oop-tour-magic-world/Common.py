from DB import DataBase


class CommonClass():
    def __init__(self):
        self.GREET = "Adios!!!"
        self.EXIT_PROCESS = "Saliendo del programa..."
        self.connectionDB = DataBase()

    def greeting(self):
        print(self.GREET)

    def salir_programa(self):
        print(self.EXIT_PROCESS)
        exit()
