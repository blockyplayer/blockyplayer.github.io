import math
import leet
seed = round((math.sqrt(math.factorial(3)))**3) / 7.348469228 

def encrypt(inp):
    string = leet.leet_translate(string)
    for alph in string:
        alph = (ord(alph) + 1) ** seed
        alph = round(alph, 0)
        alph = int(alph)
        alph = chr(alph)

def decrypt(inp):
    string = leet.string_translate(string)
    for alph in string:
        alph = ((ord(alph) - 1) ** (1/seed)) - 1
        alph = round(alph, 0)
        alph = int(alph)
        alph = chr(alph)
