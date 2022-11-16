# import colorgram
# color=colorgram.extract('hirst.jpg',20)
# rgb=[]
# for colors in color:
#     r=colors.rgb.r
#     g=colors.rgb.g
#     b=colors.rgb.b
#     t=(r,g,b)
#     rgb.append(t)
# print(rgb)
import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)
t.hideturtle()
t.setheading(225)
t.penup()
t.forward(300)
t.setheading(0)


color_list = [(253, 252, 246), (247, 254, 251), (252, 243, 249), (242, 249, 252), (235, 229, 99), (18, 114, 167),
              (163, 80, 48), (208, 159, 92), (186, 13, 63), (131, 180, 201), (230, 78, 49), (36, 137, 84), (7, 35, 89),
              (148, 163, 37), (76, 41, 22), (166, 48, 91), (113, 186, 165), (223, 120, 149), (20, 169, 208),
              (62, 159, 92)]
no_of_dot=100
t.penup()
for dot_count in range(1,no_of_dot+1):
    t.dot(10, random.choice(color_list))
    t.forward(50)

    if dot_count%10==0:

        t.setheading(90) #face the turtle up so that it can print another line
        t.forward(50)
        t.setheading(180) # move turtle left
        t.forward(500)    #move to starting of new line as 50*10 where 10 is the number of dots  steps
        t.setheading(0)


screen = Screen()
screen.exitonclick()
