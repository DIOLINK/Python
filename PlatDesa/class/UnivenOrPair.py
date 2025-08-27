class UnivenOrPair:
    MESSAJE = [
        "Es ", 
        "Par!!", 
        "Impar!!", 
        "Ingrese un numero entero: ", 
        "Intente nuevamente", 
        "Desea continuar Si ~ No: ", 
        "Adios!!"
    ]
    ZERO = 0
    VALUE_EXIT = 's'
    CRITERION = 2

    def __init__(self):
        self.is_exit = True

    def on_exit(self):
        print(self.MESSAJE[5], end='')
        value = input()
        if value.lower() != self.VALUE_EXIT.lower():
            print(self.MESSAJE[6])
            self.is_exit = False

    def is_pair(self):
        while self.is_exit:
            print(self.MESSAJE[3], end='')
            
            try:
                value = int(input())
                res = self.MESSAJE[2]
                
                if value % self.CRITERION == self.ZERO:
                    res = self.MESSAJE[1]
                
                print(self.MESSAJE[0] + res)
                self.on_exit()
            except ValueError:
                print("Por favor ingrese un número entero válido")


if __name__ == "__main__":
    user = UnivenOrPair()
    user.is_pair()
