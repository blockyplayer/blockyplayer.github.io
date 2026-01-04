import time
import os
import sys

path = os.path.expanduser('/Users/nassemnabil/Mac Storage/Epiccombat Site/blockyplayer.github.io/python/')
x = 0
fib = ['0', '1', '1']
def fibgen():
    open(f'{path}/Fibonacci.txt', 'w').close()
    with open(f'{path}Fibonacci.txt', 'a') as f:
        for i in fib:
            print(f'{i}|\n\n')
            f.write(f'{i}|\n\n')
        for i in range(end+1):
            x = fib[-2] + fib[-1]
            fib.append(x)
            sys.set_int_max_str_digits(99999999)
            string = f'{i}| {x}\n\n'
            print(string)
            f.write(string)
            # print(x, fib.index(x), len(str(x))) I was trying to find a pattern, as I noticed a nice mountain shape when they were printed
            # # time.sleep(0.1)
    f.close()
'''
IMPORTANT, DEFINE FUNC TO SAVE LAST DIGITS OF SEQUENCE FROM FILE, DEFINE AS GLOBAL, THEN USE IN BELOW FUNC
'''

'''
It appears that reading the end of a file is quite multi-faceted and can be approached by a number of methods, of varying efficiency.
The following is solved here: https://stackoverflow.com/questions/845058/how-to-get-the-line-count-of-a-large-file-cheaply-in-python/27518377?r=Saves_UserSavesList#27518377
'''
# Source - https://stackoverflow.com/a/27518377
# Posted by Michael Bacon, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-03, License - CC BY-SA 4.0

from itertools import (takewhile, repeat)

def rawincount(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum(buf.count(b'\n') for buf in bufgen)

def fibgen_append():
    with open(f'{path}Fibonacci.txt', 'r') as f:
        lines = [int(f.readlines()[(rawincount('Fibonacci.txt'))-1]), int(f.readlines()[(rawincount('Fibonacci.txt'))-2])]
    fib.append(lines)
    return(lines, fib)
fibgen_append()
# while __name__ == '__main__':
#     inp = input('Continue from last?(y/n) ')
#     end = input('Fibonacci last index: ')
#     print(get_end())
#     # if 'y' in inp.lower():
#     #     fibgen_append(end)
#     # elif 'n' in inp.lower():
#     #     fibgen(end)
#     # else:
#     #     print('An unexpected error occurred')
