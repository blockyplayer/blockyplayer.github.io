def place():
    obj = input("Enter object (optional, leave blank for default): ")
    opt = input("view save or revert save, add, remove: ").lower()
    if opt in ["revert save"]:
        coords = open('Position system/coord_save.rtf', "w")
        coords.write("")
    elif opt in ['add']:    
        pos = input("Enter x y coordinates for object (10*10 grid): ")
        with open('Position system/coords_save.rtf', "a") as coords:
            if obj in ['', ' ']:
                obj = "⊠"
            else:
                obj = obj
            x = int(pos[0])
            y = 10 - int(pos[-1]) - 1
            coords.write(pos)
            for i in range(y):
                print('')
            print(' '*x,end='')
            print(obj)
            for i in range(10 - y):
                print('')
    
    elif opt in ['remove']:
        pos = input("Enter x y coordinates for object (10*10 grid): ")
        with open('Position system/coords_save.rtf', "a") as coords:
            if obj in ['', ' ']:
                obj = "⊠"
            else:
                obj = obj
            x = int(pos[0])
            y = 10 - int(pos[-1]) - 1
            coords.write(pos)
            coords.write(' \n')
    coords.close()
place()