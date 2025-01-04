import math
import time
#import random

#image banner 
txt = open("ascii.txt", "r").readlines()
x = -1
for i in range(37):
    x = x+1
    print(txt[x], end='')
print()

#inputs

angle_attack = math.radians(float(input('Angle of Attack : ')))
height = float(input('Height (m): '))

#constants, acceleration_avg exception.
mass = 45530.8

coefficent_drag = 0.5
acceleration_avg = 4.3636
u = 0
t = 0
G = 6.67*(10**(-11))
radius_Earth = 6.371*(10**6)
g = (G * mass) / (radius_Earth+height)**2 #g=GM/r^2
full_weight = g * mass
air_density = 1.225 * (1-(height/100000))
thrust =  209066.42

while True:
    thrust_input = float(input('Thrust (-1, 1): '))
    t = t + 1
    #horizontal
    a = (thrust_input * thrust) / mass
    velocity = (a + u) - (coefficent_drag * air_density * u * (36.45 * 28.88))
    a = (591 - velocity) #decrease acceleration with time exponentially, by balancing the factor of increase

    #vertical 
    lift = (1/2 * (air_density/(height**2)) * (velocity**2) * 91.04)
    full_weight = lift / (math.degrees(math.sin(90-angle_attack)))
    
    print(f'{t}s: {round(velocity, 1)}  knots')
    time.sleep(0.1)
    u = velocity
    
#print(thrust)
#print(full_weight)
#print(thrust)