import os
import random
import string
import base64
import time
import requests, time, colorama
from random import randint
from time import sleep
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True, strip=True, convert=True)
from requests import get
from time import sleep
from pathlib import Path
# Меню. Добро пожаловать.
menu = ('• Добро пожаловать в DiscordTokenGenerator.\n \n • Как вы поняли, здесь присутствует режим генерации токенов и проверка токена на валидность...')
# Файл tokens.txt не существует.
newfile = ('• Подождите, файл tokens.txt не создан...')
file = ('• Файл tokens.txt успешно создан.')
delay = float(0.5)

os.remove('tokens.txt')

print(menu)
# Создание tokens.txt
print('• Проверка...')
time.sleep(0.5)
print(newfile)
time.sleep(1)

if os.path.exists("tokens.txt"): 
     print (filecheck)
else: 
     print (file)
     file1 = open("tokens.txt", 'w')
# Генерация токенов
time.sleep(0.5)
n = int(input("• Введите кол-во токенов: "))
count = 0

try:
    while(int(count) < n):
        tokens = []
        base64_string = "=="
        while(base64_string.find("==") != -1):
            sample_string = str(randint(000000000000000000, 999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = "\n" + base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                          for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
            count += 1
            tokens.append(token)
            file = open("tokens.txt", 'a')
            file.write(token)
finally: 
    print('• Успешно.')
# Чекер токенов
try:
    with open("tokens.txt") as f:
        for line in f:
            token = line.strip("\n")
            headers = {'Authorization': token}

            url = "https://discordapp.com/api/v9/users/@me/library"
            r = requests.get(url, headers=headers)

            if r.status_code == 200:
                print(Fore.WHITE + "[" + Fore.GREEN + "+" + Fore.WHITE + "]" + Fore.LIGHTWHITE_EX + " {} сработал.".format(line.strip("\n")))
            else:
                print(Fore.WHITE + "[" + Fore.RED + "-" + Fore.WHITE + "]" + Fore.LIGHTWHITE_EX + " {} не сработал.".format(line.strip("\n")))

            time.sleep(delay)
finally:
    print(f"• Работа завершена.")
    time.sleep(100)

    
