class Divide:
    ZERO = 0
    MESSAJE = [
        "El resultado de la divicion entre ", 
        "a: ", 
        "b: ", 
        " y ", 
        " es: ", 
        "Valor no valido!!", 
        "Ingrese la un valor para ", 
        "Intente nuevamente!!", 
        "Desa continuar Si ~ No: ", 
        "Adios!!"
    ]
    VALUE_EXIT = 's'

    def __init__(self):
        self.is_exit = True

    def is_valid_value(self, value):
        if value == self.ZERO or value != value:  # NaN check
            return False
        return True

    def on_exit(self):
        print(self.MESSAJE[8], end='')
        value = input()
        if value.lower() != self.VALUE_EXIT.lower():
            print(self.MESSAJE[9])
            self.is_exit = False

    def divide_a_to_b(self):
        while self.is_exit:
            print(self.MESSAJE[6] + self.MESSAJE[1], end='')
            
            try:
                a = float(input())
                print(self.MESSAJE[6] + self.MESSAJE[2], end='')
                b = float(input())

                if self.is_valid_value(b):
                    resul = a / b
                    print(self.MESSAJE[0] + self.MESSAJE[1] + str(a) + self.MESSAJE[3] + self.MESSAJE[2] + str(b) + self.MESSAJE[4] + str(resul))
                    self.on_exit()
                else:
                    print(self.MESSAJE[5])
                    print(self.MESSAJE[7])
            except ValueError:
                print(self.MESSAJE[5])
                print(self.MESSAJE[7])


if __name__ == "__main__":
    user = Divide()
    user.divide_a_to_b()
