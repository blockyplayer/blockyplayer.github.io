def place():
    obj = input("Enter object (optional, leave blank for default): ")
    opt = input("add, remove, or revert save: ").lower()
    if opt in ["revert save"]:
        coords = open('Position system/coord_save.rtf', "w")
        coords.write("")
    else:    
        pos = input("Enter x y coordinates for object (10*10 grid): ")
        with open('Position system/coords_save.rtf', "a") as coords:
            if obj in ['', ' ']:
                obj = "⊠"
            else:
                obj = obj
            x = int(pos[0])
            y = 10 - int(pos[-1]) - 1
            for i in range(y):
                print('')
                coords.write(' \n')
            print(' '*x,end='')
            print(obj)
            coords.write(' '*x)
            coords.write(obj)
            for i in range(10 - y):
                print('')
                coords.write(' \n')
    coords.close()
place()
