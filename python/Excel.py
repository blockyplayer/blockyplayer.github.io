from pathlib import Path
from os import chdir

print()
user = input("Enter method (upload or enter data). Type 'help' for command terms: ").lower()
if user in ['enter', 'data']:
    print('Function not programmed yet.')
elif user in ['up', 'upload', 'file']:
    user = input('Path: ')
    chdir(user)
    print(Path.cwd())
elif user in ['help', '']:
    print('Command terms:\nData (you will then be prompted to enter data directly into the terminal\nUpload [path]')