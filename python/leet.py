leet_dict = {
    'a': '@',
    'b': '6',
    'c': '<',
    'd': 'd',
    'e': 'e',
    'f': '#',
    'g': '9',
    'h': '|-,',
    'i': '!',
    'j': ')',
    'k': 'k',
    'l': '7',
    'm': '|\\|\\',
    'n': ':-,',
    'o': '0',
    'p': 'p',
    'q': '*1',
    'r': '|2',
    's': '5',
    't': '+',
    'u': '|_1',
    'v': R'v',
    'w': R'\/\/',
    'x': 'x',
    'y': '\'/',
    'z': 'z',
    'A': '^',
    'B': '|3',
    'C': '(',
    'D': 'D',
    'E': '3',
    'F': '|=',
    'G': 'C;',
    'H': '}{',
    'I': '1',
    'J': '.)',
    'K': '|{',
    'L': '7',
    'M': '|v|',
    'N': '|\\|',
    'O': '0',
    'P': '|>',
    'Q': '0,',
    'R': '|x',
    'S': '$',
    'T': '`|`',
    'U': '|_|',
    'V': '\\/',
    'W': '\\/\\/',
    'X': '}{',
    'Y': '`/',
    'Z': '`/_'
}

def leet_translate():
    inp = input('Enter string: ')
    # for word, leet in leet_dict.items():
    #     inp= inp.replace(word, leet)
    inp = inp.translate(str.maketrans(leet_dict))
    return inp
def string_translate():
    inp = input('Enter leet: ')
    for k,v in leet_dict.items():
        inp = inp.replace(v, k)
    return inp
print(leet_translate())
print(string_translate())

