import colorama, fade, os, sys, time
from colorama import Fore
from modules.common import *


def main():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    set_console_title('retexts dev build | made by clairesfanboy')

    banner = """
                         :::::::::  :::::::::: ::::::::::: :::::::::: :::    ::: ::::::::::: :::::::: 
                        :+:    :+: :+:            :+:     :+:        :+:    :+:     :+:    :+:    :+: 
                       +:+    +:+ +:+            +:+     +:+         +:+  +:+      +:+    +:+         
                      +#++:++#:  +#++:++#       +#+     +#++:++#     +#++:+       +#+    +#++:++#++   
                     +#+    +#+ +#+            +#+     +#+         +#+  +#+      +#+           +#+    
                    #+#    #+# #+#            #+#     #+#        #+#    #+#     #+#    #+#    #+#     
                   ###    ### ##########     ###     ########## ###    ###     ###     ########       

                                         ╔═══════════════════════════════╗
                                         ║ [1] Close                     ║
                                         ║ [2]                           ║
                                         ║ [3]                           ║
                                         ║ [4]                           ║
                                         ║ [5]                           ║
                                         ║ [6]                           ║
                                         ║ [7]                           ║
                                         ║ [8]                           ║
                                         ║ [9]                           ║
                                         ╚═══════════════════════════════╝
"""
    faded = fade.pinkred(banner)
    print(faded)

    print_info()

    # get user input
    user_input = input(f"\t${Fore.LIGHTRED_EX}:{Fore.WHITE}>> ")
    if user_input == '1':
        reset_banner()
        print_info()
        closing = f"""{Fore.LIGHTRED_EX}\t\t\t\t\t   exiting, see you next time <3 \n"""
        print(closing)
        time.sleep(2)
        sys.exit()


while True:
    main()