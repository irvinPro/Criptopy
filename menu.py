import console as cons
import fernet as fernet

class menu(object):
    opc = False
    submenu1 = False
    
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
        