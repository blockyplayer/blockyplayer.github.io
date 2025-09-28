import time
from motion import char
import random


def intuit():
    r = random.randint(18, 72)
    j = 0
    k = 0
    l = 0
    with open('intu.txt', 'r+') as f:
        num = int(input('What is the number: '))
        f.write(f'{num}')
        f.seek(0)
        for i in range(r):
            if j > 8:
                j = 0
            if k > 8:
                k = 0
            print(f'\r{char['seq4'][j]} Extrapolating {char['seq6'][k:k+3]}', end='\r')
            print(f'')
            # print(f'''\n\rHello''', end='\r')
            j += 1
            k += 3
            time.sleep(0.25)
        time.sleep(0.2)
        print('')
        for i in range(r-9):
            
            for i in range(len(str(f.readlines))):
                if l > 10 or l < -9:
                    l = 0
                print(f'\r{(char['seq9'][l-i])*len(str(num))}', end='\r')
            # print(f'\r{char['seq9'][l]}{char['seq9'][l-1]}{char['seq9'][l-2]}', end='\r')
            # l = l + 1
            time.sleep(0.2)
            for i in f.readlines():
                print(f'\r{i}', end='\r')

intuit()
