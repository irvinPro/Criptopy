# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography
    
def get_opcion_estegano(submenu2):
     while True:    
         if submenu2 == 1:             
             ocultar_mensaje()
             break
         elif submenu2 == 2:
             get_mensaje()
             break            
         elif submenu2 == 3:         
             print("Salir")
             break                 
         else:
             input("Opcion no valida")
             submenu2 = int(input("Introduzca opcion valida:"))
             get_opcion_estegano(submenu2)
             return True
             
def ocultar_mensaje():
    print("Formatos soportados: JPG, BMP, GIF, PNG.")
    path = input("Ruta de archivo:")
    print("Se solicita ruta del archivo a crear")
    output_path = input("Ruta nueva:")
    msg = input("Ingrese mensaje: ")    
    Steganography.encode(path, output_path, msg)
    print("Se ha guardado la imagen la ruta:",output_path)
    input("Precione para continuar...")

def get_mensaje():
    print("Mostrando mensaje oculto...")
    path = input("Nombre de archivo:")
    secret_text = Steganography.decode(path)                 
    print(secret_text)
    input("Precione para continuar...")