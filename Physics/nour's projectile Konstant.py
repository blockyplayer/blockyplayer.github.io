import math
import time

#constants
k1 = 14500
k2 = 303.15
k3 = 36000
k4 = 10
k5 = 9000
k6 = 12000
dynamic_drag = 0.26
g = 19.05 #knots/s^-2
thrust2weight_ratio = 7.75
capcity_engine = 14300 #N
v = 0 #initialise with zero velocity

#inputs
thrust = float(input('Thrust(-1, 1): ')) * capcity_engine
height = float(input('Height(feet): '))
angle_attack = math.radians(float(input('Angle of Attack(deg): ')))
timestamp = float(input('Value Return Iteration Time(sec): '))
wind = float(input('Wind direction(x,y,z)deg: '))
temperature = float(input('Thermal temperature(degC): '))

#simulation loop
while True:
#   v = ((thrust*thrust2weight_ratio)/(k1+height) - (thrust/(k1+height)*25 - temperature)**0.25 + v-(((v*dynamic_drag)**2) * k2) / (k3+height) - g*(k3/(k3+height)) * math.degrees(math.sin(angle_attack)))
    v = (thrust/(k1+height)) * ((temperature+k2+273.15)**2) * (1/k3) + v - (((v*0.26)**2) * k4/(k5+height)) - (g*k6/(k6+height)) * math.sin(angle_attack)
    print(v)
    time.sleep(timestamp)