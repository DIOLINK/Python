from ProgramUtil import ProgramUtil

class SumNumber(ProgramUtil):
    ZERO = 0

    def __init__(self):
        super().__init__()
        message = [
            "Ingrese un numero entero positivo, cero para salir: ", 
            "No es un valor valido", 
            "El resultado de sumar 1 hasta ", 
            " es: ", 
            "Adios!!"
        ]
        self.init(*message)

    def on_error(self):
        print(self.MESSAGES[1])

    def cal(self):
        while self.EXIT:
            print(self.MESSAGES[0], end='')
            
            try:
                value = int(input())
                
                if value < self.ZERO:
                    self.on_error()
                elif value == self.ZERO:
                    self.EXIT = False
                else:
                    aux = 0
                    for i in range(1, value + 1):
                        aux += i
                    print(self.MESSAGES[2] + str(value) + self.MESSAGES[3] + str(aux))
            except ValueError:
                self.on_error()
        
        print(self.MESSAGES[4])


if __name__ == "__main__":
    user = SumNumber()
    user.cal()
