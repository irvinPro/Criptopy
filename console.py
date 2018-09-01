from termcolor import colored
from colorama import init
import os


def banner():
    logo = """
 _____      _       _                     
/  __ \    (_)     | |                    
| /  \/_ __ _ _ __ | |_ ___   _ __  _   _ 
| |   | '__| | '_ \| __/ _ \ | '_ \| | | |
| \__/\ |  | | |_) | || (_) || |_) | |_| |
 \____/_|  |_| .__/ \__\___(_) .__/ \__, |
             | |             | |     __/ |
             |_|             |_|    |___/ 
 ------------------------------------------------
   """
    cls()
    init()
    print(colored(logo,'red'))


def cls():
    os.system('cls')


def section(name):
    print("\n{} {}".format(
        colored("::", 'blue', attrs=['bold']),
        colored(name, attrs=['bold'])
        )
    )
def failure(name):
    print('{} {}'.format(
        colored("==> ERROR:", 'red', attrs=['bold']),
        colored(name, attrs=['bold'])
        )
    )

def instrucciones_Opcion1():
    banner()
    msg = """
   +-+-+-+-+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+    
 |S|E|L|E|C|C|I|O|N|A| |U|N|A| |O|P|C|I|O|N|    
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+    
 |1|)|G|e|n|e|r|a|c|i|o|n| |d|e| |h|a|s|h|      
 +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+      
 |2|)|C|i|f|r|a|d|o| |d|e| |m|e|n|s|a|j|e|      
 +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
 |3|)|D|e|s|c|i|f|r|a|d|o| |d|e| |m|e|n|s|a|j|e|
 +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+
 |4|)|S|a|l|i|r|                                
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
  """    
    print(colored(msg,'yellow'))

def instrucciones_Opcion2():
    banner()
    msg = """
 +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+
 |F|o|r|m|a|t|o|s| |A|c|e|p|t|a|d|o|s|:|
 +-+-+-+-+-++-+-+-++-+-+-+-+-++-+-+-++-+
   |J|P|G|  |P|N|G|  |B|N|P|  |G|I|F|   
   +-+-+-+  +-+-+-+  +-+-+-+  +-+-+-+   
  """    
    print(colored(msg,'yellow'))
    