#wind = input('Wind direction(speed,x,y,z): ').split(',')
#wind = [float(i) for i in wind]

#print(wind[1] + wind[2])
height = int(input('height: '))
air_density = 1.225 * (1-(height/100000))
print(air_density)