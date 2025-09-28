# Henceforth proceed functions useful for situations demanding specific answers
string = any

def length(string):
    string = (input('Enter String: ').split(' '))
    print(f'\n{len(string)} words\n\n{len(' '.join(string))} characters\n\n{len(''.join(string))} characters excluding spaces\n')

while True:
    length(string)