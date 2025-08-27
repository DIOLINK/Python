class ValidateStorePass:
    MESSAJE = [
        "Correcta!!", 
        "Incorrecta!!", 
        "Ingrese la clave: ", 
        "Intente nuevamente"
    ]
       
    def __init__(self, *arr_pass):
        self.store_pass = list(arr_pass)
        self.is_exit = True
    
    def validate_pass(self, pass_input):
        for value_pass in self.store_pass:
            if value_pass.lower() == pass_input.lower():
                return True
        return False
    
    def is_validate(self):
        while self.is_exit:
            print(self.MESSAJE[2], end='')
            pass_input = input()
            
            if self.validate_pass(pass_input):
                print(self.MESSAJE[0])
                self.is_exit = False
            else:
                print(self.MESSAJE[1])
                print(self.MESSAJE[3])


if __name__ == "__main__":
    passwords = ["VVIRKvysEZj5S4", "VpP1Y9JXQ5psrl", "casI13245"]
    user = ValidateStorePass(*passwords)
    user.is_validate()
