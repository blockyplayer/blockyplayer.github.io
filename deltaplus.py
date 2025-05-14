def linear():
    fx = input('Enter linear equation (y=mx+c): ').lower()

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

    print(f'm = {m}, c = {c}')

    obj = 'O'

    # if '-' not in fx:
    #     c = int(-c)
    x = 10
    # if m >= 3:
    #     obj = '|'
    # elif m < 3:
    #     obj = '/'
    print('^')

    while x > 1:
        for i in range(m-1):#logic to leave space for obj
            print('|') #move cursor downwards by m amount
            y = round((m * x) + c)
        print(f'|{' '*(x-2)}', end='')#-2 because there are two characters printed on the line
        print(obj)
        x = x - 1
    # print(obj)
    # for i in range(c):
    #     print('|')
    for i in range(c):
        print('|') 
    print(f'{'﹉'*7}>')
        
while True:
    linear()