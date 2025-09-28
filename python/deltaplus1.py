def linear():
    
    obj = 'O'
    fx = input('Enter linear equation (y=mx+c): ').lower()
    if 'x' in fx:
        #testing if there is a value for c, if not it is 0
        if fx[-1] == 'x':
            c = 0
        else:
            c = int(fx.partition('x')[-1])

        #testing if there is a value for m, if not it is 1
        if fx[0] == 'x':
            m = 1
        elif fx[0] != 'x':
            m = int(fx.partition('x')[0])
        else:
            m = int(input('Value for {y[0]}? '))
    else:
        m = 0
        c = int(fx)
    print(f'm = {m}, c = {c}')
    x_lim = (0-c)/m
    if m > 0:
        x = 10
    elif m < 0:
        x = 0
    else:
        x = -0
    # # if c < 0 and abs(c) > m:
    # #     x = 
    

    # if '-' not in fx:
    #     c = int(-c)
    # if m >= 3:
    #     obj = '|'
    # elif m < 3:
    #     obj = '/'
    print('^')
    while x > 1 and m > 0:
        if x == 10:
            print(f'|{' '*8}{obj}')
            x = x - 1
        else:
            for i in range(m-1): #logic to leave space for obj
                print('|') #move cursor downwards by m amount
                y = round((m * x) + c)
            print(f'|{' '*(x-2)}', end='')#-2 because there are two characters printed on the line
            print(obj)
        x = x - 1
    if m == 0:
        print('^\n|')
        print(f'|{obj*10}')
    # print(obj)
    # for i in range(c):
    #     print('|')
    if c > 0 and m > 0:
        for i in range(m-1): #m-1 to leave new line for obj
            print('|')
        print(obj)
        for i in range(c-1): #c-1 to leave new line for obj
            print('|')
        print(f'|{'-'*10}>')
    elif c < 0 and abs(c) < m:
        print(f'|{'-'*10}>')
        for i in range(m-2):
            print('|')
        print(f'{obj}\n|')
    # # elif c < 0 and abs(c) > m:
    # #     print(f'|{'-'*10}>')      HEELLP
    # #     for i in range()
    # # elif m == c:
    elif m < 0 and c > 0:
        print(f'|\n{obj}')
        while x < x_lim:
            for i in range(abs(m)-1):
                print('|')
            print(f'|{' '*(x-2)}{obj}')
            x = x + 1
        print(f'|{'-'*10}>')
    else:
        for i in range(c):
            print('|') 
        print(f'|{'-'*10}>')
        
while True:
    linear()