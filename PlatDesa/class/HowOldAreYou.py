class HowOldAreYou:
    OLD_AGE = 18
    ZERO = 0
    MAX_AGE = 150
    MESSAGES = [
        "Cuantos años tienes?: ",
        "Mayor",
        "Menor", 
        "Ingresar solo el numeros que correspondan a tu edad",
        "No es un valor valido!!.",
        "Error: MENSAJES no puede estar vacío", 
        "Adios!!"
    ]
    
    def __init__(self):
        self.EXIT = True
    
    def validate_age(self, age):
        if age <= self.ZERO or age >= self.MAX_AGE:
            print(self.MESSAGES[4])
            self.EXIT = False
            print(self.MESSAGES[6])
        return age
   
    def is_old(self, age):
        if self.OLD_AGE <= age:
            print("Eres " + self.MESSAGES[1] + " de edad!")
        else:
            print("Eres " + self.MESSAGES[2] + " de edad!")
    
    def ask(self):
        while self.EXIT:
            print(self.MESSAGES[3])
            print(self.MESSAGES[0], end='')
            
            try:
                age_input = input()
                age = self.validate_age(int(age_input))
                
                if self.EXIT:
                    self.is_old(age)
            except ValueError:
                print(self.MESSAGES[4])
                self.EXIT = False
                print(self.MESSAGES[6])


if __name__ == "__main__":
    user = HowOldAreYou()
    user.ask()
