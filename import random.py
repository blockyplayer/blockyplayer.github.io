import random

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]
url = 'https://blockyplayer.github.io/'
en = 'abcdefghijklmnopqrstuz'

for i in range(len(url)):
    x = fib[-2] + fib[-1]
    y = x - fib[-1]
    fib.append(x)
    for j in y:
        new = f'{url[:]}'
    print(f'{url[i]}')
