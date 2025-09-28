pref = input('Operation (e.g integrate): ').lower()
dx = input('X value range ({x1 x2} or leave blank to find general equation): ').split(' ')
func = input('Function (y=m x + c): ').split(' ')
if dx != '':
    y1 = int(func[0]) * int(dx[0]) + int(func[-1])
    y2 = int(dx[1])
    dy = y2 - y1
    print({dy})
# def integrate():
#     if 'integrat' in pref:
#         for i in range():