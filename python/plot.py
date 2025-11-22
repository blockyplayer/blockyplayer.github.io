x = input('Enter x-values                                              : ').split(',')
y = input('Enter corresponding y-values (match with the x-values above): ').split(',')
z = []

for i in range(len(x)):
    z.append(tuple(x[i]+y[i]))
    z.sort(key=(z[i])[1])
print(z)
