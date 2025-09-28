import math
import random
thrust = 0
def physics_737():
    empty_weight  = 5204.38
    coefficent_drag = 0.000075
    thrust = input('Throttle Power: ')
    thrust = float(thrust) * 98300 * (1 - coefficent_drag)
    angle_attack = math.radians(float(input('Angle of Attack <=\|=^: ')))
    angle_rot = float(input('Angle of Rotation -Ộ-: '))
    lift = 130000 - 5204.38
    net_force = (lift ** 2 + thrust ** 2) ** 1 / 2
    g = 9.81
    v = math.sin(1.944 * (((net_force) / empty_weight / g)))
    v = (math.degrees(v) ** (1 / math.cos(v))) - (angle_attack * (math.degrees(math.sin(angle_attack) * 2) - 10*angle_attack)) * (random.randint(7, 10) / 10)
    print((v/1.5)-(0.4*v)+20)

while thrust != '':
    physics_737()