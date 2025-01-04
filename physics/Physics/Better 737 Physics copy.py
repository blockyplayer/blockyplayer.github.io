import math
import time
import random

txt = open("ascii.txt", "r").readlines()
x = -1
for i in range(37):
    x = x+1
    print(txt[x], end='')
print()

#constants, acceleration_avg exception.
g = 9.81
mass = 45530.8
full_weight = g * mass 
coefficent_drag = 0.5
acceleration_avg = 4.3636
u = 0
t = 0
G = 0.0000000000666

#inputs
thrust_input = float(input('Thrust (-1, 1): ')) 
angle_attack = math.radians(float(input('Angle of Attack : ')))
height = float(input('Height (m): '))
g = (G * mass) / (height**2)

while True:
    t = t + 1
    #horizontal
    velocity = (((coefficent_drag * thrust_input * mass * (591 - velocity) * 0.0366666) - (u * coefficent_drag)) + (mass * u)) / mass #v=Ft+mu/m   , then converted to knots
    
    #vertical 
    lift = (1/2 * 1.225 * (velocity**2) * 91.04)
    full_weight = lift / (math.degrees(math.sin(90-angle_attack))) #increase acceleration with time exponentially, by balancing the factor of increase
    
    print(f'{t}s: {round(velocity, 1)}  knots')
    time.sleep(0.001)
    u = velocity
    
#print(thrust)
#print(full_weight)
#print(thrust)