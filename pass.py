import pyautogui as gui
import time
import os

os.system('open -a Firefox')
time.sleep(2.5)
gui.leftClick(960, 540)
time.sleep(1)
user = 'nour.nabil@education.nsw.gov.au'
for i in range(11):
    pswd = f'TheQuantumMechanic5.{i}.0'
    gui.hotkey('command', 't')
    time.sleep(1)
    gui.write('https://portal.education.nsw.gov.au/studentPortal/index.html')
    gui.hotkey('enter')
    time.sleep(5)
    gui.write(user)
    gui.hotkey('tab')
    time.sleep(1)
    gui.write(pswd)
    gui.hotkey('enter')
    time.sleep(5)