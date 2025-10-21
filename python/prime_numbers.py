import time
import os
import sys

# % finds the remainder of x / y e.g 6 % 3 is 0 and 9 % 6 is 3
# Prime numbers can only be odd, but if you are looking for numbers not divisable by anthing, this should be in
# the same algorithm anyway

x = 3
y = list(range(2, 10))
primes = [1, 3, 5, 7]

while True:
    for i in y:
        if any((x % i) == 0):
            prime = False
        else:
            prime = True
    if prime:
        print(x)
    x += 2