# obj = input('Enter a character to animate: ')
# runtime = input('How many frames (blank for infinite loop): ')
# # dict = {
# #         'yes': 'no', 
# #         'once': 'never',
# #         True: False
# # }
# # print(dict['yes'])
# # print(int(dict[True]))
import time

char = {
    'seq0': '⌜⁀⌝⌉⌋⌟‿⌞⌊⌈',
    'seq1': '⇑⇗⇒⇘⇓⇙⇐⇖  ',
    'seq2': '☝⇗☞⇘☟⇙☜⇖  ',
    'seq3': '(⁀)‿(⁀)‿  ',
    'seq4': '╚╔╗╝╚╔╗╝  ',
    'seq5': "'i;. 'i;. ",
    'seq6': '.  .. ... ',
    'seq7': '|/-\\|/-\\  ', #trailing spaces to account for escaped characters, avoiding 
    'seq8': '!@#$%^&*:;',
    'seq9': '17425683902'}
i = 0
j = 0
x = 0
y = 0

def uno():
    for i in range(9):
        return f'\r{char['seq0'][i]}'

def dos():
    for i in range(9):
        return f'\r{char['seq1'][i]}'

def tres():
    for i in range(9):
        return f'\r{char['seq2'][i]}'

def quatro():
    for i in range(9):
        print(f'\r{char['seq3'][i]}')

def sinco():
    for i in range(9):
        print(f'\r{char['seq4'][i]}')

def seis():
    for i in range(9):
        return f'\r{char['seq5'][i]}'

def all():
    j = 0
    while True:
        if j > 9:
            j = 0
        for i in range(11): # length of longest string, other strings must be up to this length too
            print(f'\r{char[f'seq{j}'][i]}', end="\r")
            time.sleep(0.25)
        j = j + 1

if __name__ == "__main__":
    all()
# for i in range(5):
#     print(char[f'seq{j}'][i])
#     i = i + 1