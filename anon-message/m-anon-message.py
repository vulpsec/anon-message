#!/usr/bin/python3
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'#

import os
import sys
import requests

print(RED+"{}Her İP Yalnız Bir Kez{}{} SMS Atabilir. Proxy (VPN,Tor v.b) Açarak Daha Falza Sms Atabilirsiniz.\n".format(UNDERLINE,END,RED)+END)
print(RED+"{}{}BU TOOL TAMAMEN ANONİM DEĞILDIR{}{}, KÖTÜ AMAÇLI KULLANIMINIZDA PROX'YE DE GÜVENMEYİN!!".format(UNDERLINE,BOLD,END,RED)+END)

while True:
    print(BOLD+"""
    ____          _          _   ____
   / ___|___   __| | ___  __| | | __ ) _   _
  | |   / _ \ / _` |/ _ \/ _` | |  _ \| | | |
  | |__| (_) | (_| |  __/ (_| | | |_) | |_| |
   \____\___/ \__,_|\___|\__,_| |____/ \__, |
                                        |___/
{} __  __            _     _                            
|  \/  | ___  _ __| |__ (_)_   _ ___   ___  ___            
| |\/| |/ _ \| '__| '_ \| | | | / __| / _ \/ __|                
| |  | | (_) | |  | |_) | | |_| \__ \| (_) \__ \                    
|_|  |_|\___/|_|  |_.__/|_|\__,_|___(_)___/|___/        
{}                                                                
Author: {}
Instagram: {}
Github: {}
    """.format(YELLOW,GREEN, AUTHOR, INSTAGRAM, GİTHUB) +END)
    target = input('Sms Kime({}905xxxxxxxxx Şeklinde Yazınız{}): '.format(BOLD,END))
    mesaj = input('Göndermek İstediğiniz Mesaj: ')
    a = ' '
    if a ==target:
        sys.exit()
    elif a == mesaj:
        sys.exit()
    else:
        response=requests.post('https://textbelt.com/text' , data={
        'phone':'{}'.format(target),
        'message':'{}'.format(mesaj),
        'key':'textbelt' })
        print('İşlem: {}, kalan hakkınız {}'.format('Başarılı!'if response.json()['success'] == 'True' else 'Başarısız!', response.json()['quotaRemaining']))
        exit = input('Çıkmak için "exit" yazınız, devam etmek için "Enter" a basınız.')
        if exit == 'exit':
            sys.exit()
        else:
            os.system(clear)
            pass