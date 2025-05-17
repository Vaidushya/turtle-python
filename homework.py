import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.pensize(3)
t.pencolor("black")
t.speed(3)

def draw_square(side_length):
    for i in range(4):
        t.forward(side_length)
        t.right(90)

draw_square(100)
t.hideturtle()
screen.exitonclick()