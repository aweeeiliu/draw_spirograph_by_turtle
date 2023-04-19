import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.shape("triangle")
screen = Screen()


def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

# for i in range(4):
#     tim.fd(100)
#     tim.right(90)
# for i in range(3, 10):
#     tim.circle(150, 360, i)
#     abc = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     aaa = tuple(abc)
#     tim.pencolor(aaa)

# for i in range(25):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# def gogo(side):
#     angle = 360/side
#     for _ in range(side):
#         tim.fd(100)
#         tim.right(angle)
#
#
# for i in range(3, 11):
#     gogo(i)
#     abc = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     aaa = tuple(abc)
#     tim.pencolor(aaa)

# direction = (0, 90, 180, 270)
# tim.pensize(5)
# tim.speed(9)
# for i in range(30):
#     head_to = random.choice(direction)
#     tim.setheading(head_to)
#     tim.fd(30)
#     abc = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     tim.color(abc)


tim.speed(0)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(6)

screen.exitonclick()
