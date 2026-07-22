import turtle

t = turtle.Turtle()
t.speed(3)
t.pensize(6)


t.penup()
t.goto(-23, 51)
t.pendown()


t.setheading(40)
t.forward(30)


t.setheading(270)
t.forward(120)


t.penup()
t.goto(-30, -50)
t.pendown()
t.setheading(0)
t.forward(60)

t.hideturtle()
turtle.done()
