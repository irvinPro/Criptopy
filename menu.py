import console as cons
import fernet as fernet
import estegano as estegano

class menu(object):
    opc = False
    submenu1 = False
    submenu2 = False
    
    def __init__(self):
        cons.banner()                
        print("1) Criptografia")
        print("2) Estenografia")
        print("3) Salir")
        self.opc = int(input(" ... "))

    def menu_Encriptar(self):
        while True:        
            cons.instrucciones_Opcion1()           
            print("1) Generacion de hash")
            print("2) Cifrado de mensaje")
            print("3) Descifrado de mensaje")
            print("4) Salir")
            self.submenu1 = int(input(" ... "))
            if self.submenu1 != 4:
                fernet.get_opcion_fertnet(self.submenu1)
            else:
                break

    def menu_Estegano(self):
        while True:
            cons.instrucciones_Opcion2()
            print("1) Ocultar mensaje")
            print("2) Mostrar mensaje")
            print("3) Salir")
            self.submenu2 = int(input(" ... "))
            if self.submenu1 == 3:
                break
            else:
                estegano.get_opcion_estegano(self.submenu2)
                break
            