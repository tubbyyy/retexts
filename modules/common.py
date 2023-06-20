import colorama, os, sys, time
import fade
from colorama import Fore


def print_info():
    info = f"""{Fore.LIGHTRED_EX}\t\t\t\t\t       made by clairesfanboy \n"""
    for value in info:
        time.sleep(0.0001)
        sys.stdout.write(value)
        sys.stdout.flush()
    print()

def reset_banner():
    banner = """
                         :::::::::  :::::::::: ::::::::::: :::::::::: :::    ::: ::::::::::: :::::::: 
                        :+:    :+: :+:            :+:     :+:        :+:    :+:     :+:    :+:    :+: 
                       +:+    +:+ +:+            +:+     +:+         +:+  +:+      +:+    +:+         
                      +#++:++#:  +#++:++#       +#+     +#++:++#     +#++:+       +#+    +#++:++#++   
                     +#+    +#+ +#+            +#+     +#+         +#+  +#+      +#+           +#+    
                    #+#    #+# #+#            #+#     #+#        #+#    #+#     #+#    #+#    #+#     
                   ###    ### ##########     ###     ########## ###    ###     ###     ########   
    """
    faded = fade.pinkred(banner)

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(faded)


def set_console_title(text:str):
    sys.stdout.write(f"\x1b]2;{text}\x07")
