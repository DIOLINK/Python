from datetime import datetime, date
from ProgramUtil import ProgramUtil

class AgeTaxAction(ProgramUtil):
    OLD_AGE = 18
    MAX_AGE = 150
    LIMIT_TRX = 1000000

    def __init__(self):
        super().__init__()
        message = [
            "Ingrese su fecha de nacimiento (dd/mm/yyyy): ", 
            "Igrese el ingreso para el mes ", 
            "Fecha de naciomiento no valida", 
            "Si, ", 
            "No, ", 
            "debe tributar",
            "Adios!!"
        ]
        self.init(*message)
        self.objects = {}
        self.date_current = datetime.now()
        self.month_current = self.date_current.month
        self.CONT = 1

    def on_error_date(self):
        print(self.MESSAGES[2])
        self.EXIT = False

    def get_name_months(self, num_month):
        months = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
            5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
            9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }
        return months.get(num_month)

    def cal(self):
        aux = 0
        res = self.MESSAGES[4]
        
        for value in self.objects.values():
            aux += float(value)
        
        if aux >= self.LIMIT_TRX:
            res = self.MESSAGES[3]
        
        print(res + self.MESSAGES[5])

    def cal_tax_action(self):
        print(self.MESSAGES[0], end='')
        birth_date_str = input()
        
        try:
            # Parsear fecha en formato dd/mm/yyyy
            parts = birth_date_str.split('/')
            if len(parts) == 3:
                birth_date = datetime(int(parts[2]), int(parts[1]), int(parts[0]))
                
                today = datetime.now()
                diff_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                
                if diff_years < self.OLD_AGE or diff_years >= self.MAX_AGE:
                    self.on_error_date()
                
                if self.EXIT:
                    self.ask_for_income()
            else:
                print("Formato de fecha inválido. Use dd/mm/yyyy")
                self.on_error_date()
        except (ValueError, IndexError):
            print("Formato de fecha inválido. Use dd/mm/yyyy")
            self.on_error_date()

    def ask_for_income(self):
        if not self.EXIT:
            return
        
        month_name = self.get_name_months(self.CONT)
        if not month_name:
            return
        
        print(self.MESSAGES[1] + month_name + ":", end='')
        value = input()
        self.objects[month_name] = value
        
        if self.CONT == self.month_current:
            self.cal()
            print(self.objects)
            print(self.MESSAGES[6])
            self.EXIT = False
        else:
            self.CONT += 1
            self.ask_for_income()


if __name__ == "__main__":
    user = AgeTaxAction()
    user.cal_tax_action()
