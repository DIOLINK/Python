
import admin
import getch
import login
import pwinput
import socio

titulo = "MENÚ DE INICIO DE SESIÓN"


def salir_programa():
    print("Saliendo del programa...")
    exit()

def main():
    print(titulo)
    print("-" * len(titulo))
    while True:
        # VERIFICAR SI SE PRESIONÓ LA TECLA "ESC"
        print("Presione cualquier tecla para continuar o Esc para finalizar...")
        tecla = getch.getch()
        if tecla.lower() == chr(27):
            salir_programa()

        email = input("Ingresar mail: ").lower()
        # REMPLAZA LOS LETRAS CON *
        clave = pwinput.pwinput(prompt='Ingresar clave: ')
        # clave = input("Ingresar clave: ")

        perfil = login.validar_login(email, clave)

        if perfil == "socio":
                socio.mostrar_menu()
        elif perfil == "admin":
                admin.mostrar_menu()
        else:
                print("Credenciales no válidas. Reintentar")

if __name__ == "__main__":
    main()