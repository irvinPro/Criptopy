from menu import menu
#import console
#import console
# Put this somewhere safe!
if __name__ == "__main__":
    
     while True:    
         M = menu()
      
         if M.opc == 1:
             M.menu_Encriptar()             
         elif M.opc == 2:             
             M.menu_Estegano()
         elif M.opc == 3:         
             break
         else:
             input("Opcion no valida")
             
     print ("Fin")