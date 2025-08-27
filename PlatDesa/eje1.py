class AgeUser:
    OLD_AGE = 18
    ZERO = 0
    MAX_AGE = 150
    MESSAGES = [
        "¿Cuántos años tienes?: ",
        "Mayor",
        "Menor",
        "Ingresar solo números que correspondan a tus años",
        "¡No es un valor válido!"
    ]

    @staticmethod
    def main():
        print(AgeUser.MESSAGES[3])
        age = input(AgeUser.MESSAGES[0])
        res = AgeUser.MESSAGES[2]
        try:
            age = int(age)
            if age <= AgeUser.ZERO or age >= AgeUser.MAX_AGE:
                print(AgeUser.MESSAGES[4])
            elif AgeUser.OLD_AGE <= age:
                res = AgeUser.MESSAGES[1]
            print(f"Eres {res} de edad!")
        except ValueError:
            print(AgeUser.MESSAGES[4])


if __name__ == "__main__":
    AgeUser.main()
