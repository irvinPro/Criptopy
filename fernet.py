from cryptography.fernet import Fernet
import pyperclip
# Put this somewhere safe!

def get_opcion_fertnet(submenu1):
     while True:    
         if submenu1 == 1:
             print("Generador de hash")
             opcion1_generar_hash()
             break
         elif submenu1 == 2:
             print ("Cifrado de mensaje")
             cifradoMensaje()
             break            
         elif submenu1 == 3:         
             print("Descifrado de mensaje")
             descifradoMensaje()
             break
         elif submenu1 == 4:
             print("Salir")
             break
         else:
             input("Opcion no valida")
             return False


def opcion1_generar_hash():    
    key = Fernet.generate_key()
    print("LLave generada: ",key)
    srt_key = key.decode()
    pyperclip.copy(srt_key)
    print("Se copio el hash al portapapeles")
    input("Presiona para continuar...")
    
def cifradoMensaje():    
    srt_key = input("Ingrese el hash:") 
    key = str.encode(srt_key)
    print(key)
    msg = str.encode(input("Ingrese un mensaje:"))
    f = Fernet(key)
    token = f.encrypt(msg)
    srt_token = token.decode()
    pyperclip.copy(srt_token)
    print("Se copio el mensaje al portapapeles")
    input("Presiona para continuar...")
    
def descifradoMensaje():
    srt_key = input("Ingrese el hash:") 
    key = str.encode(srt_key)
    msg = str.encode(input("Ingrese el mensaje codificado: "))
    f = Fernet(key)
    tokenreversr = f.decrypt(msg)
    print("Mensaje resuelto:",tokenreversr.decode())
    input("Presiona para continuar...")    