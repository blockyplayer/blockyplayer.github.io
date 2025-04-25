def linear():
    y = input('Enter linear equation (y=mx+c): ')
    #testing if there is a value for c, if not it is 0
    if y[-1] != 'x':
        c = int(y[-1])
    else:
        c = 0
    #testing if there is a value for m, if not it is 1
    if y[0] == 'x':
        m = 1
    elif y[0] != 'x':
        m = int(y[0])
    else:
        m = int(input('Value for {y[0]}? '))
    obj = '/'
    if '-' not in y:
        c = int(-c)
        x = 5
        if m >= 3:
            obj = '|'
        elif m < 3:
            obj = '/'
        for i in range(5):
            y = int((m * x) + c)
            print(' '*x, end='')
            print(obj)
            if m != 1:
                for i in range(m-1):
                    print('')
            else:
                print('\n')
            x = x - 1
        if c > 0:
            for i in range(c):
                print(' ')
                print('- '*20,end='')
                print('>')
        elif c == 0:
            print('- '*20,end='')
            print('>')

while True:
    linear()