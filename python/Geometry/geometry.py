import math 


shape = input('Enter shape: ').lower()
length = input('Enter base and height in order (cm): ').split()
base = int(length[0])
height = int(length[-1])

if shape in ['triangle']:
    hypotenuse = (base**2 + height**2)**0.5 #pythagoreas
    x = 0
    if height > base:
        base = int(length[0]) + int(round(height-base, 1))
    for i in range(round(height, 1)):
        print(' '*base ,end='')
        print('/' ,end='')
        print(' '*x ,end='')
        print('|')
        base = base - 1
        x = x + 1
    if height > base:
        base = int(length[0]) + int(round(height-base, 1))
        print('─'*int(round((base - (height/base))/2)))
    else:
        print('─'*(base/3))
elif shape in ['cicrle']:
    for i in range(10):
        x = 1
        print(f'Kevin bruh {x} {base, height}')
        x = x + 1
elif shape in ['rectangle', 'square']:
    if shape in ['square']:
        height == base
        height = height / 2
    print(' ',end='')
    print('─'*base)
    for i in range(int(round(height, 1))):
        print('|', end='')
        print(' '*base,end='')
        print('|')
    print(' ',end='')
    print('─'*base)
    print(f'A = {int(round(int(length[0])))*int(round(int(length[-1])))} cm^2')
    print(f'P = {2 * (int(round(int(length[0])))+int(round(int(length[-1]))))} cm')


# if shape in ['triangle']:
#     hypotenuse = (base**2 + height**2)**0.5 #pythagoreas
#     turtle.pendown()
#     turtle.speed(10)
#     theta = int(round(math.atan(height / base)))
#     alpha = int(round(180 - (theta + 90)))
#     turtle.right(90)
#     turtle.forward(height)
#     turtle.right(90)
#     turtle.forward(base)
#     turtle.right(42.5+alpha)
#     turtle.forward(hypotenuse)
#turtle.done()