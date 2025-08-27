from HowOldAreYou import HowOldAreYou
from ValidateStorePass import ValidateStorePass
from Divide import Divide
from UnivenOrPair import UnivenOrPair
from AgeTaxAction import AgeTaxAction
from SumNumber import SumNumber
from SumAllNum import SumAllNum

class Ejers:
    MESSAGES = [
        "=== MENÚ PRINCIPAL ===",
        "1. HowOldAreYou - Verificar edad",
        "2. ValidateStorePass - Validar contraseña",
        "3. Divide - División de números",
        "4. UnivenOrPair - Verificar par/impar",
        "5. AgeTaxAction - Cálculo de impuestos por edad",
        "6. SumNumber - Suma de números consecutivos",
        "7. SumAllNum - Suma de todos los números",
        "0. Salir",
        "Seleccione una opción: "
    ]

    @staticmethod
    def main():
        while True:
            print("\n" + "="*50)
            for message in Ejers.MESSAGES:
                print(message)
            
            try:
                option = int(input())
                
                if option == 1:
                    print("\n=== HowOldAreYou ===")
                    user = HowOldAreYou()
                    user.ask()
                elif option == 2:
                    print("\n=== ValidateStorePass ===")
                    passwords = ["VVIRKvysEZj5S4", "VpP1Y9JXQ5psrl", "casI13245"]
                    user = ValidateStorePass(*passwords)
                    user.is_validate()
                elif option == 3:
                    print("\n=== Divide ===")
                    user = Divide()
                    user.divide_a_to_b()
                elif option == 4:
                    print("\n=== UnivenOrPair ===")
                    user = UnivenOrPair()
                    user.is_pair()
                elif option == 5:
                    print("\n=== AgeTaxAction ===")
                    user = AgeTaxAction()
                    user.cal_tax_action()
                elif option == 6:
                    print("\n=== SumNumber ===")
                    user = SumNumber()
                    user.cal()
                elif option == 7:
                    print("\n=== SumAllNum ===")
                    user = SumAllNum()
                    user.cal()
                elif option == 0:
                    print("¡Adiós!")
                    break
                else:
                    print("Opción no válida. Presione Enter para continuar...")
                    input()
                    
            except ValueError:
                print("Por favor ingrese un número válido")
                input()


if __name__ == "__main__":
    Ejers.main()
