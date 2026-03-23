import turtle
screen = turtle.Screen()
screen.bgcolor("white") 


pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(2) 
pen.color("red", "yellow")


def draw_petal():
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

for _ in range(5):
    draw_petal()
    pen.right(72) 


pen.color("yellow", "yellow")
pen.begin_fill()
pen.circle(20)
pen.end_fill()
turtle.done()
