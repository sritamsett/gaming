import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(270)
t.pendown()

t.left(25)
t.forward(40)
t.left(130)
t.forward(40)

t.right(180)
t.forward(60)
t.circle(-10,90)
t.penup()
t.forward(250)

turtle.done()