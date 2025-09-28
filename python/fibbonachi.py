import time
import os
import sys
path = os.path.expanduser('/Users/nassemnabil/Library/CloudStorage/OneDrive-NSWDepartmentofEducation/AWORKUSB/IST Legacy/joke python/')
x = 0
fib = [0, 1, 1]
# while x < 999999:
with open(f'{path}fibbonachi.txt', 'w') as f:
    print('0\n1\n1')
    # f.write('0\n1')
    for i in range(99):
        x = fib[-2] + fib[-1]
        fib.append(x)
        sys.set_int_max_str_digits(9999999)
        print(x)
        # f.write(f'{str(x)}\n')
        # print(x, fib.index(x), len(str(x))) I was trying to find a pattern, as I noticed a nice mountain shape when they were printed
        # # time.sleep(0.1)
f.close()