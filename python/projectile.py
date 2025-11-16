'''
The program rounds every value to one decimal place, because it is not possible to print half-lines or half-characters
in the terminal. It would be much easier to use the turtle module to illustrate the projectile's exact path,
however, this is the easy way and I am not known for choosing comfort over commitement.

"Soon, we must all face the choice between what is right and what is easy"
- Albus Percival Wulfric Brian Dumbledore

'''

from math import cos, sin

g = 9.81 #ms^-2

u = int(input('Initial velocty (ms^-1): '))
theta = int(input('Angle above the horizontal (degrees): '))

t = 2 * (u/g)
sx = t * u*cos(theta)
h = (u*sin(theta)*t) + (0.5*g*(t**2))
x = sx
print(f'\nTime: {t} seconds\nHorizontal range: {sx} metres\nHeight: {h} metres\n')
gradient = (round(h))/(round(sx)) 
zt = round((1/gradient)*h)
z = round((1/gradient)*h)
for i in range(round(h)):
    x += sx
    z = z - round(1/gradient)
    print(f'{' '*round(z/2)}/{' '*(z-round(z/2))}|')
print('_'*round(sx))

for i in range(round(h)):
    x += sx
    z = z - round(1/gradient)
    print(f'{' '*round(z/2)}/{' '*(zt-round(zt/2))}|')
print('_'*round(sx))    

for i in range(round(h)):
    x += sx
    z = z - round(1/gradient)
    print(f'{' '*round(z/2)}/{' '*(zt-round(z/2))}|')
print('_'*round(sx))

for i in range(round(h)):
    x += sx
    z = z - round(1/gradient)
    print(f'{' '*round(z/2)}/{' '*(z-round(zt/2))}|')
print('_'*round(sx))

print(gradient)
print(1/gradient)