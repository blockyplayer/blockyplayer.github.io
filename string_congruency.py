# Check if two strings are the same, including captiliasation and punctuation
string = input('''Enter first string: ''')
string2 = input('''Enter second string: ''')

if string == string2:
    print('The strings are the same.')
elif string != string2:
    print('They are not equal.')
else:
    print('An error occured. Check syntax and try again.')