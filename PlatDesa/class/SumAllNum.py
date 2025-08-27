from ProgramUtil import ProgramUtil

class SumAllNum(ProgramUtil):
    ZERO = 0

    def __init__(self):
        super().__init__()
        message = [
            "Ingrese numeros enteros positivo, ó ingesar un numero negativo para salir: ", 
            "El resultado de la suma es: ", 
            "Adios!!"
        ]
        self.init(*message)

    def cal(self):
        aux = 0
        
        while self.EXIT:
            print(self.MESSAGES[0], end='')
            
            try:
                value = int(input())
                
                if value < self.ZERO:
                    self.EXIT = False
                else:
                    aux += value
            except ValueError:
                print("Por favor ingrese un número entero válido")
        
        print(self.MESSAGES[1] + str(aux))
        print(self.MESSAGES[2])


if __name__ == "__main__":
    user = SumAllNum()
    user.cal()
