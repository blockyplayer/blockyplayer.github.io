from math import cos, sin

g = 9.81 #ms^-2

u = int(input('Initial velocty (ms^-1): '))
theta = int(input('Angle above the horizontal (degrees): '))

t = 2 * (u/g)
sx = t * u*cos(theta)
h = (u*sin(theta)*t) + (0.5*g*(t**2))
x = sx
print(f'Time: {t} seconds\nHorizontal range: {sx} metres\nHeight: {h} metres')
gradient = (round(h))/(round(sx))
for i in range(round(h)):
    x += sx
    if round(1/gradient) % x == 0:
        print(f'{' '*(round(sx/2)-x-1)}/{' '*x}|')
    else:
        print(f'{' '*(round(sx/2))}|',)
    gradient = (round(h))/(round(sx))
print('_'*round(sx))
print(gradient)
print(1/gradient)