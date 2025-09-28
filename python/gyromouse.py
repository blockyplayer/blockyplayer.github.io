import pyautogui as gui
import os
import time

1648, 343
pix_per_scroll = 16

n_scroll = int(input('How many scrolls? (best effect on long pages): '))
gui.moveTo(1464, 160)
gui.leftClick()
time.sleep(1)
gui.hotkey('command', 't')
time.sleep(1)
gui.write('https://en.wikipedia.org/wiki/Michael_Jackson', 0)
time.sleep(1)
gui.hotkey('enter')
gui.moveTo(1500, 990)

time.sleep(1.25)
for i in range(n_scroll):
    for i in range(16):
        gui.scroll(-1)
        gui.moveRel(0, -16, duration=0.09)