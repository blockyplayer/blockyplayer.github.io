import time
import pyautogui as gui
import random as r
import os
screenWidth, screenHeight = gui.size()
currentMouseX, currentMouseY = gui.position()
rand = r.randint(0, 1)
search = ' '

while search != '':
    search = input('Thirsty for information? ').lower()

    if search in ['no', 'n', 'incorrect', 'nah', 'meh']:
        with open('lazy_browser_banner.txt', 'r') as f:
            print(f.read())
    elif search in ['special']:
        while True:
            gui.FAILSAFE = False
            gui.moveTo(1920, 540)
            gui.moveTo(0, 540)
    else:
        f = None
    if rand == 0:
        gui.moveTo(1111, 1040, r.randint(0, 2))
        gui.leftClick()
        time.sleep(0.5)
        gui.hotkey('command', 't')
        gui.write('https://en.wikipedia.org/wiki/Special:Random', interval=0.25)
        gui.hotkey('enter')
    elif rand == 1:
        os.system("open -a Firefox")
        gui.hotkey('command', 't')
        gui.write('https://en.wikipedia.org/wiki/Special:Random', interval=0)
        gui.hotkey('enter')