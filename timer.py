
import time
import pygame
pygame.init()

warning = pygame.mixer.Sound('507502__elanhickler__argi_scifi_alarm_tracking_05.wav')
tick = pygame.mixer.Sound('57211__mab__mab-clock-tick-1-20080713.wav')
stopwatch = ""
def clock(stopwatch):
    stopwatch = input("Duration (with units after): ")
    stopwatch = stopwatch.lower()
    vector = input("Count up or down? ")
    vector = vector.lower()
    if stopwatch != "":
        user = stopwatch.split()
        unit = user[1]
        duration = int(user[0])

        if unit[0] == "s":
            rest = 1
        elif unit[0] == "m":
            rest = 60
        elif unit[0] == "h":
            rest = 3600
        else:
            rest = 1

        if "up" in vector:
            for durations in range(duration):
                print(durations)
                tick.play()
                time.sleep(rest)
                durations = duration - 1
        elif "down" in vector:
            for durations in range(duration):
                print(duration)
                tick.play()
                time.sleep(rest)
                duration = duration - 1
        print("**TIMER UP**")
        warning.play(20)

    else:
        print("**!AN UNEXPECTED ERROR OCCURED!**")

while 1 < 2:
    clock(stopwatch)