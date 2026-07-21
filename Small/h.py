import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 0)
t.setheading(90)
t.pendown()

t.forward(140)
t.left(180)
t.penup()
t.forward(90)
t.left(180)
t.pendown()

t.circle(-30, 180)
t.forward(50)



turtle.done()
