import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(270)
t.pendown()

t.left(25)
t.forward(60)
t.left(130)
t.forward(45)
t.right(130)
t.forward(45)
t.left(130)
t.forward(60)


turtle.done()