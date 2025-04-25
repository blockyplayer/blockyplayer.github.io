num = ""
arith = ""
num2 = ""
user = "."

def calc(num, arith, num2):
    user = input("Expression: ")
    user = user.lower()
    if user == "":
        print("PROGRAM TERMINATED")
    elif user != "":
        userl = user.split()
        arithl = ['+', '-', '*', '/', '^', 'v', 'sci']

        if userl[0] == "v":
            num = float(userl[-1])
            arith = userl[0]
            num2 = float(userl[-1])
        elif userl[1] in arithl:
            num = float(userl[0])
            arith = userl[1]
            num2 = float(userl[2])
        elif userl[1] == 'sci':
            arith = userl[1]
            num = userl[0]
            num2 = userl[-1]
        
        if arith == "+" and num2 != arith:
            print(f"{float(num)} + {float(num2)} = {float(num)+float(num2)}")
        elif arith == "-" and num2 != arith:
            print(f"{float(num)} - {float(num2)} = {float(num)-float(num2)}")
        elif arith == "*" and num2 != arith:
            print(f"{float(num)} * {float(num2)} = {float(num)*float(num2)}")
        elif arith == "/" and num2 != arith:
            print(f"{float(num)} / {float(num2)} = {float(num)/float(num2)}")
        elif arith == "^" and num2 != arith:
            print(f"{float(num)} ^{float(num2)} = {float(num)**(float(num2))}")
        elif arith == "v":
            print(f"√{float(num)} = {float(num)**(1/2)}")
        elif arith == "sci" and str(num[0]) == '0':
            numsci = f'{num[1:]}.{num[:1]}'
            numr = round(numsci, 2)
            numf = len(numsci) - 2
            print(f'{numr}x10^-{numf}') 
        elif arith == "sci" and str(num[0]) != '0':
            numsci = f'{num[:1]}.{num[1:]}'
            numr = round(float(numsci), 2)
            numf = len(numsci) - 2
            print(f'{numr}x10^{numf}') 
    else:
        print("!**AN UNEXPECTED ERROR OCCURED**!")

calc(num, arith, num2)