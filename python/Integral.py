fx = '3x+5'
def func():
    fx = input('Enter function: ')
    dx = input('Enter x values (comma-separated): ').strip('').split(',')
    y1 = fx.replace('x', dx[0])
    if 'x' in fx and 'sys' not in fx:
        a = int(dx[0])
        b = int(dx[-1])
        print(f'Differential: {(eval(fx.replace('x', 'a'))-eval(fx.replace('x', 'b')))/(a - b)}') #dy/dx
        
while fx != '':
    func()