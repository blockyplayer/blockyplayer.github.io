import pyautogui as gui
import time
screenWidth, screenHeight = gui.size()
posX, posY = gui.position()

while True:
    posX, posY = gui.position()
    gui.moveTo(posX, posY+20, 0.1)
    time.sleep(0.1)
    gui.moveTo(posX, posY-21, 0.1)