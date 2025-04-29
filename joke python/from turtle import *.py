from turtle import *

length = int(input("Length? "))
pencolor("green")
        
pensize(5)
angle = 144
for i in range(5):
  forward(length)
  right(angle)