import math
import random
phoo = random.randint(0, 100)
seed = round((math.sqrt(math.factorial(3)))**3) / phoo 
string = " "

def encrypt(string):
    string = input("Encrypt: ")
    string = string.lower()
    string = string.replace("a", "t")
    for alph in string:
        alph = (ord(alph) + 1) ** seed
        alph = round(alph, 0)
        alph = int(alph)
        print(chr(alph))

def decrypt(string):
    string = input("Decrypt: ")
    string = string.lower()
    for alph in string:
        alph = ((ord(alph) - 1) ** (1/seed)) - 1
        alph = round(alph, 0)
        alph = int(alph)
        alph = chr(alph)
        finalalph = alph.replace("t", "a")
        print(finalalph)

while string != "":
    print(phoo)
    encrypt(string)
    decrypt(string)