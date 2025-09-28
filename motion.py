obj = input('Enter a character to animate: ')
runtime = input('How many frames (blank for infinite loop): ')
x = 10
y = 0
if runtime == '':
    while True:
        y = y + 1
        if y == 0 or y % 10 == 0 and y % 20 !=0:
            x = x + 1
        elif y % 10 != 0 and y > 10:
            x = x - 1
        print(' '*x, end='')
        print(obj)
else:
    runtime = int(runtime)
    for i in range(runtime):
        y = y + 1
        print(' '*x, end='')
        print(obj)
        if y == 0 or y % 10 == 0 and y % 20 !=0:
            x = x + 1
        elif y % 10 != 0 and y > 10:
            x = x - 1