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

        try:
            age = int(age)
            if age <= AgeUser.ZERO or age >= AgeUser.MAX_AGE:
                print(AgeUser.MESSAGES[4])
            elif AgeUser.OLD_AGE <= age:
                print(f"Eres {AgeUser.MESSAGES[1]} de edad!")
            else:
                print(f"Eres {AgeUser.MESSAGES[2]} de edad!")
        except ValueError:
            print(AgeUser.MESSAGES[4])


if __name__ == "__main__":
    AgeUser.main()
