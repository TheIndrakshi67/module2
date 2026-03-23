import turtle
import time
t=turtle.Turtle()
turtle.Screen().bgcolor("white")
t.shape("circle")
t.color("red", "yellow")
t.speed(0)

for i in range (36):
    t.stamp()
    t.forward(100)
    t.right(170)
    time.sleep(1)

turtle.done()