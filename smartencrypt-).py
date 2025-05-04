import math
import random
import numpy as np
dtype=np.int64
foo = random.randint(0, 10)
seed = round((math.sqrt(math.factorial(3)))**3) / 7.348469228 + foo
string = " "

def encrypt(string):
    string = input("Encrypt: ")
    string = string.lower()
    string = string.replace('a', 't')
    string = string.replace('e', 'z')
    if len(string) <= 10:
        for alph in string:
            alph = (ord(alph) + 1) ** seed + foo
            alph = round(alph, 0)
            alph = int(alph)
            print(chr(alph))
    elif len(string) > 10 and len(string) < 30:
        bytelen = len(string)
        bitlen = len(string) / 2
        bit1 = string[0:bitlen]
        bit2 = string[bitlen:bytelen]
        for alph in bit1:
            alph = (ord(alph) + 1) ** seed + foo
            alph = round(alph, 0)
            alph = int(alph)
            print(chr(alph))
        for alph in bit2:
            alph = (ord(alph) + 1) ** seed + foo
            alph = round(alph, 0)
            alph = int(alph)
            print(chr(alph))
    else:
        print("ERROR")

def decrypt(string):
    string = input("Decrypt: ")
    string = string.lower()
    for alph in string:
        alph = ((ord(alph) - 1) ** (1/seed)) - 1 - foo
        alph = round(alph, 0)
        alph = int(alph)
        alph = chr(alph)
        alph = alph.replace('t', 'a')
        alph = alph.replace('z', 'e')
        print(alph)

while string != "":
    encrypt(string)
    decrypt(string)