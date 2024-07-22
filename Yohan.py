import random
import time
import colorama
import os
from os import system, name
from time import sleep
from pystyle import Write, Colors, Colorate, Box
from colorama import Fore, Back, Style

colorama.init()
import time
import random


#functions
def g(rolls):
  data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
  result = ""
  while rolls >= 1:
    c = random.choice(data)
    result = c + result
    rolls = rolls - 1
  return result

Write.Print(f'''
╭
██╗░░░██╗░█████╗░██╗░░██╗░█████╗░███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░██║██╔══██╗████╗░██║
░╚████╔╝░██║░░██║███████║███████║██╔██╗██║
░░╚██╔╝░░██║░░██║██╔══██║██╔══██║██║╚████║
░░░██║░░░╚█████╔╝██║░░██║██║░░██║██║░╚███║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
''', Colors.green_to_cyan, interval=0.005)
print(Colorate.Vertical(Colors.green_to_cyan, "𝕿𝖍𝖊 𝖚𝖑𝖙𝖎𝖒𝖆𝖙𝖊 𝖗𝖊𝖕𝖑𝖎𝖙 𝖌𝖊𝖓 𝖙𝖔𝖔𝖑", 1))
print()
print()

print(Colorate.Vertical(Colors.green_to_cyan, "Made by, perwah1", 1))
print()
print(Colorate.Vertical(Colors.green_to_cyan, " Join The Server Below For More Support", 1))
print()
print(Colorate.Vertical(Colors.green_to_cyan, "note: ", 1))
print(Fore.GREEN+"All Unchecked")
print()
print("")
text = "https://discord.gg/6qD8yC9T"
print(Colorate.Color(Colors.cyan, text, True))
Write.Print(f"updating to working tools soon", Colors.green_to_cyan, interval=0.1)
print()
print(Fore.GREEN+"updates will be paid")
print()
print(Fore.GREEN)


print(Colorate.Horizontal(Colors.green_to_cyan, "input the number corresponding to the item", 1))
print(Colorate.Vertical(Colors.green_to_cyan, '''
╔══════════════════════════════════════╗
║[1] Amazon Store Card Gen             ║
║[2] Discord Nitro Gen + Checker       ║
║[3] Netflix Gift Code Gen             ║
║[4] Xbox Gift Card Gen                ║
║[5] Playstation Gift Card Gen         ║
║[6] Nitro gen & checker updated 2/3   ║ 
║[7] Token gen                         ║
║[8] ps4 cards                         ║
║[9] Other (not checked)               ║
║-----------------tools----------------║
║[10] load apple gen                   ║
║[11] load VT2 gen                     ║
║[12] load Energy SMM                  ║
║---------------multitools-------------║
║[13] load okuru                       ║
║[14] load AMIZ                        ║
╚══════════════════════════════════════╝
''', 14))
print(Fore.LIGHTGREEN_EX)
choice = int(input("number:  "))

if choice == 1:
  import random
  import time
  import colorama
  from colorama import Fore, Back, Style
  colorama.init()

  class validator():

    def __init__(self):
        self.cardNumber = None
        self.Brand = None

    def __findBrand(self):
        if self.cardNumber[:2] in ['34', '37']:
            self.Brand = 'American Express'
        elif self.cardNumber[:3] in ['300', '301', '302', '303', '304', '305']:
            self.Brand = 'Diners Club - Carte Blanche'
        elif self.cardNumber[:2] in ['36']:
            self.Brand = 'Diners Club - International'
        elif self.cardNumber[:2] in ['54']:
            self.Brand = 'Diners Club - USA & Canada'
        elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in ['644', '645', '646', '647', '648',
                                                                         '649'] or self.cardNumber[0:2] in [
            '65'] or self.cardNumber[0:6] in [str(x) for x in range(622126, 622926)]:
            self.Brand = 'Discover'
        elif self.cardNumber[:3] in ['637', '638', '639']:
            self.Brand = 'InstaPayment'
        elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
            self.Brand = 'JCB'
        elif self.cardNumber[:4] in ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']:
            self.Brand = 'Maestro'
        elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'] or self.cardNumber[:6] in [str(x) for x in
                                                                                              range(222100, 272100)]:
            self.Brand = 'MasterCard'
        elif self.cardNumber[:4] in ['4026', '4508', '4844', '4913', '4917'] or self.cardNumber[:6] == '417500':
            self.Brand = 'VISA Electron'
        elif self.cardNumber[0] in ['4']:
            self.Brand = 'VISA'
        else:
            self.Brand = 'Unknown Brand'

    def validate(self, number):
        """
        number: str or int credit card number
        """
        if number is None: return 'Not a valid Credit Card Number'
        if number is bool: return 'Not a valid Credit Card Number'
        if number is float: return 'Not a valid Credit Card Number'
        number = ''.join(x for x in str(number).strip().split())
        if number.isdigit() and 13 <= len(number) <= 19:
            # Identify Brand
            self.cardNumber = number
            self.__findBrand()
            # Luhn's Algorithm
            lastDigit = int(number[-1])
            base = [int(x) for x in reversed(number[:-1])]
            base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
            base = [x if x <= 9 else x - 9 for x in base]
            base = sum(base)
            base = (base * 9) % 10
            if base == lastDigit:
                print(Fore.GREEN)
                return f'[!] {self.cardNumber} is a valid Store Card!'
                file = open("cards.txt", "w")
                number = repr(number)
                file.write(number)
                file.close()
            else:
                print(Fore.RED)
                return f'[!] {self.cardNumber} is not a valid Store Card!'
        else:
            return 'Not a valid Credit Card Number'

  print(Fore.LIGHTGREEN_EX + " ")
  print("1. 1k Card")
  print("2. 2k Card")
  print("3. 5k Card")
  print("4. 10k Card") 
  print(" ")
  whatcard = input("[?] What Card Do You Want To Generate? (1, 2, 3 or 4) ")
  print(" ")
  whatcard = int(whatcard)
  randomnums = "0123456789"

  if whatcard == 1:
    howmany = input("[?] How Many Cards Do You Want? ")
    time.sleep(0.8)
    print("[/] Starting")
    time.sleep(0.8)
    howmany = int(howmany)

    for x in range(howmany):
        bin = "60457811425"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))

  if whatcard == 2:
    howmany = input("How Many Cards Do You Want? ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578114"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
        print(validator().validate(int(cc)))

  if whatcard == 3:
    howmany = input("How Many Cards Do You Want? ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "604578118"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
        print(validator().validate(int(cc)))

  if whatcard == 4:
    howmany = input("How Many Cards Do You Want? ")
    howmany = int(howmany)
    for x in range(howmany):
        bin = "6045781123"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)
        print(validator().validate(int(cc)))
elif choice == 2:
  import os
  import ctypes
  import requests
  import random
  import string
  import time
  print("")

  num = int(input('Input How Many Codes to Generate and Check: '))

  with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated!")

    start = time.time()

    for i in range(num):
      code = "".join(
        random.choices(string.ascii_uppercase + string.digits +
                       string.ascii_lowercase,
                       k=19))

      file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time generated: {time.time() - start}\n")

  with open("Nitro Codes.txt") as file:
    for line in file.readlines():
      nitro = line.strip("\n")

      url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

      r = requests.get(url)

      if r.status_code == 200:
        print( f" Valid | {nitro} ")
        break
      else:
        print( f" Invalid | {nitro} ")

  time.sleep(0.2)

  print(
    "Valid codes will be in Valid Codes.txt - if there none then keep generating :)"
  )

elif choice == 3:
  import colorama
  import random, string

  upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  lower_letter = 'abcdefghijklmnopqrstuvwxyz'
  digits = '0123456789'

  amount = int(input("Gift Code Amount : "))
  for i in range(amount):
    code = "https://www.netflix.com/redeem/" + "".join(
      random.choices(string.ascii_uppercase + string.digits, k=11))
    print("[GENERATED] " + code)
    giftcode = open('netflixcodes.txt', 'a')
    giftcode.write(code + "\n")

elif choice == 4:
  import requests
  print("Checked Xbox Gift Codes ;)")
  print("")
  print("How many of them?")
  nn = input(">")
  print("")
  n = int(nn)
  for x in range(n):
    print("")
    v = g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5) + "-" + g(5)
    url = "https://microsoft.com/api/entitlements/redeem/" + v

    s = requests.get(url)

    if s == 200:
      print(f" Valid | {v} ")
      break
    else:
      print(f" Invalid | {v} ")

  print("Done!")

elif choice == 5:
  import requests
  print("Checked PS codes")
  print("")
  print("How many of them?")
  nn = input(">")
  print("")
  n = int(nn)
  for x in range(n):
    print("")
    v = (g(4) + "-" + g(4) + "-" + g(4))
    url = "https://playstation.com/api/redeem/" + v

    s = requests.get(url)

    if s == 200:
      print(f" Valid | {v} ")
      break
    else:
      print(f" Invalid | {v} ")

elif choice == 6:
  import random, string, requests, urllib.request, urllib, urllib.parse, colorama, os, threading, green
  from colorama import Fore as C
  from colorama import Style as S
  from threading import Thread
  os.system("")
  print("Valid codes are in Valid codes.txt at the bottom")
  class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    
  def gencode():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(16))
    
  f = open("Valid codes.txt", "a+")

  class NitroGenerator:
    def __init__(self):
        self.codes = []
        self.check()
    
    def check(self):
        while True:
            code = gencode()
            self.codes.append(code)
            response = requests.get(
                "https://discord.com/api/v7/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
            data = response.json()
            if response.status_code == 200:
                print(style.GREEN + "Worked | " + code)
                f.write(f"\ndiscord.gift/{code}")
            else:
                print(style.RED + "invalid | " + code)



  NitroGenerator()

elif choice == 7:
  import random
  import string
  import pathlib
  import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib,       datetime, os.path
  import colorama
  from colorama import Fore, init, Back, Style
  from datetime import date

  os.system("title [et-exploits token gen] Made by etxnight#1010")

  def Spinner():
	   l = ['|', '/', '-', '\\']
	   for i in l+l+l:
		    sys.stdout.write('\r' + Fore.YELLOW +'Starting GEN...'+i)
		    sys.stdout.flush()
		    time.sleep(0.2)

  Spinner()

  banner = (Fore.LIGHTGREEN_EX+'''
  ╭━━━━╮╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭━━━╮
  ┃╭╮╭╮┃╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱┃╭━╮┃
  ╰╯┃┃╰╯╭━━╮┃┃╭╮╭━━╮╭━╮╱┃┃╱╰╯╭━━╮╭━╮
  ╱╱┃┃╱╱┃╭╮┃┃╰╯╯┃┃━┫┃╭╮╮┃┃╭━╮┃┃━┫┃╭╮╮
  ╱╱┃┃╱╱┃╰╯┃┃╭╮╮┃┃━┫┃┃┃┃┃╰┻━┃┃┃━┫┃┃┃┃
  ╱╱╰╯╱╱╰━━╯╰╯╰╯╰━━╯╰╯╰╯╰━━━╯╰━━╯╰╯╰╯''')

  os.system("cls")
  count = 0
  current_path = os.path.dirname(os.path.realpath(__file__))
	
  print()
  print(Fore.GREEN+"╭━━━╮╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮")
  print("┃╭━━╯╭╯╰╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╭╯╰╮")
  print("┃╰━━╮╰╮╭╯╱╱╱╱╭━━╮╭╮╭╮╭━━╮┃┃╱╭━━╮╭╮╰╮╭╯╭━━╮")
  print("┃╭━━╯╱┃┃╱╭━━╮┃┃━┫╰╋╋╯┃╭╮┃┃┃╱┃╭╮┃┣┫╱┃┃╱┃━━┫")
  print("┃╰━━╮╱┃╰╮╰━━╯┃┃━┫╭╋╋╮┃╰╯┃┃╰╮┃╰╯┃┃┃╱┃╰╮┣━━┃")
  print("╰━━━╯╱╰━╯╱╱╱╱╰━━╯╰╯╰╯┃╭━╯╰━╯╰━━╯╰╯╱╰━╯╰━━╯")
  print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃")
  print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯")
  print("𝕿𝖍𝖊 𝖚𝖑𝖙𝖎𝖒𝖆𝖙𝖊 𝖗𝖊𝖕𝖑𝖎𝖙 𝖙𝖔𝖐𝖊𝖓 𝖌𝖊𝖓 𝖙𝖔𝖔𝖑")
  print()


  print(Fore.GREEN)
  print(Fore.LIGHTGREEN_EX+"[1] "+Fore.GREEN+"Token Generator(super fast!)")
  print(Fore.LIGHTGREEN_EX+"[2] "+Fore.GREEN+"Token Checker(Checks all tokens you generated)")
  print(Fore.LIGHTGREEN_EX+"[3] "+Fore.GREEN+"Credits")
  print(Fore.LIGHTGREEN_EX+"[4] "+Fore.GREEN+"Exit")
  print(Fore.LIGHTGREEN_EX)
  opcion = input("\nChoice: ")
  if opcion=='1':
	   os.system("cls")
	   print(banner)
	   cantidad = input("\nAmount to generate: ")
	   while int(count)<int(cantidad):
		    Generated = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
		    f= open(current_path +"/"+str("Generated")+str("")+".txt","a")
		    f.write(Generated+"\n")
		    print(Fore.CYAN +"Token: "+ Fore.RESET + Generated)
		    count+=1
		    if int(count)==int(cantidad):
			     print("\n" + Fore.CYAN +Fore.RED +"Tokens generated successfully!")
			     print(Fore.WHITE +Fore.BLUE +"Tokens saved in Generated.txt")
			     input(Fore.BLUE +Fore.BLUE +"\nPress enter to exit")
			     os.system("cls")

			     print(Fore.LIGHTGREEN_EX+"Closing!")
			     print(Fore.LIGHTGREEN_EX+"Have a good day :D")

			     time.sleep(2)
			     sys.exit()
			     pass
	   pass
  if opcion=='2':
	   os.system("cls")
	   print("\n" + banner + "\n")
	   with open('Generated.txt', 'r') as f:
	    for line in f:
	        time.sleep(0)
	        token = line.rstrip("\n")
	        headers = {
	            'Authorization': f'{token}'  
	        }
	        src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

	        try:
	            if src.status_code == 200:
	                print(f'{Fore.LIGHTGREEN_EX}Valid token! >{Fore.RESET} ' + token)
	            else:
	                print(f'{Fore.RED}InValid token >{Fore.RESET} ' + token)
	        except Exception:
	            print(f"{Fore.RED}Error{Fore.RESET}")
  pass
  if opcion=='3':
	   os.system("cls")

	   print(Fore.LIGHTGREEN_EX+"TOKEN GEN"+Fore.LIGHTGREEN_EX+" Made by "+Fore.GREEN+"etxnight#7080")
	   print(Fore.LIGHTGREEN_EX+"             [Discord]  ")
	   print(Fore.GREEN+"https://discord.gg/SeaXAJJyPE")


	   input(Fore.BLUE +Fore.BLUE +"Enter to exit")
	   os.system("cls")
	
	   print(Fore.LIGHTGREEN_EX+"Closing!")
	   print(Fore.GREEN+"Have a good day :D")
	
	   time.sleep(2)
	   sys.exit()
	   pass
  if opcion=='4':
	   os.system("cls")
	
	   print(Fore.LIGHTGREEN_EX+"Closing!")
	   print(Fore.GREEN+"Have a good day :D")
	   time.sleep(2)
	   sys.exit()
	   pass
elif choice == 8:
  import requests
  print(" ")
  print(" Checked PS codes")
  print("")
  print(" How many of them?")
  print(" ")
  nn = input(f"{Fore.LIGHTGREEN_EX} ammount: ")
  print("")
  n = int(nn)
  for x in range(n):
        print("")
        v = (g(4) + "-" + g(4) + "-" + g(4))
        url = "https://playstation.com/api/redeem/" + v

        s = requests.get(url)

        if s == 200:
            print(f"{Fore.GREEN} Valid | {v} ")
            break
        else:
            print(f"{Fore.RED} Invalid | {v} ")

elif choice == 9:
  #interface
  print(
    "JUST SO YOU KNOW THESE ARE UNCHECKED SO YOU'RE GONNA HAVE TO GO FIND A CHECKER FOR YOUR CODES"
  )
  print("Multiple Gift Card Generator")
  print("")
  print("What Do You Need To Generate?")

  tt = input(
    "\n[1] Amazon\n[2] Roblox\n[3] Fortnite\n[4] Ebay\n[5] iTunes\n[6] Paypal\n[7] Visa\n[8] Playstation\n[9] Steam\n[10] Xbox\n[11] PlayStore\n[12] Minecraft\n[13] BruteForcer\n[14] Phishing\n>"
  )

  t = tt.lower()
  print("")
  print("How many of them?")
  nn = input(">")
  print("")
  n = int(nn)
  if t == "minecraft":
    for x in range(n):
      print("")
      print(g(4) + "-" + g(4) + "-" + g(4))

  if t == "paypal":
    for x in range(n):
      print("")
      print(g(4) + "-" + g(4) + "-" + g(4))

  if t == "amazon":
    for x in range(n):
      print("")
      print(g(4) + "-" + g(6) + "-" + g(4))

  if t == "netflix":
    for x in range(n):
      print("")
      print(g(4) + "-" + g(6) + "-" + g(4))

  if t == "steam":
    for x in range(n):
      print("")
      print(g(4) + "-" + g(6) + "-" + g(5))

  if t == "fortnite":
    for x in range(n):
      print("")
      print(g(5) + "-" + g(4) + "-" + g(4))

  if t == "roblox":
    for x in range(n):
      print("")
      print(g(3) + "-" + g(3) + "-" + g(4))

  if t == "itunes":
    for x in range(n):
      print("")
      print(g(16))

  if t == "ebay":
    for x in range(n):
      print("")
      print(g(10))

  if t == "playstore":
    for x in range(n):
      print("")
      print(g(4) + "-" + g(4) + "-" + g(4) + "-" + g(4) + "-" + g(4))

  print("")
  print("-----Generation completed-----")
elif choice == 10:
  #unused
  from sub1 import *
  #unused
elif choice == 11:
  #unused
  from Sub2 import *
elif choice == 12:
  #unused
  from Sub3 import *
elif choice == 13:
  print("before using nuker input settings in settings.json")
  print("Fixed by "+Fore.MAGENTA+".index")
  input(Fore.LIGHTGREEN_EX+"press enter to continue")
  from SubM1 import *
elif choice == 14:
  print("before using nuker input settings in nuker.json")
  input(Fore.LIGHTGREEN_EX+"press enter to continue")
  from SubM2 import *
  time.sleep(360)
