import math, time, random

#constants
g = 9.81 #ms^-2
empty_mass = 34564 #kg
passenger_mass = 10966.8 #kg
full_weight = g * (empty_mass + passenger_mass) #N
coefficent_drag = 0.24
acceleration_avg = 4.3636 #ms^-2
#initialisation
t = 0
u = 0
v = 0
#inputs
thrust = float(input('Thrust (-1, 1): '))
angle_attack = math.radians(float(input('Angle of Attack : ')))
thermals = float(input('Thermal temperature(degC): '))
wind = input('Wind direction(speed,x,y,z): ').split(',')
wind = [float(i) for i in wind]
wind_y = wind[0] * math.sin(wind[2])
wind_x = (wind[0]*math.cos(wind[2])) * (math.cos(wind[1]))

#calculation

#initialize simulation loop
while True:
    horizontal = (thrust * (empty_mass+passenger_mass) * coefficent_drag * acceleration_avg) - wind_x
    lift = 1/2 * 1.225 * (horizontal**2) * 91.04
    vertical = (lift - full_weight) - wind_y
    v = ((horizontal**2)+(vertical**2)**0.5)
    print(v)
    v = u
    time.sleep(0.5)