import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 0)
t.setheading(90)
t.pendown()

t.forward(90)
t.right(90)
t.penup()
t.forward(30)
t.right(180)
t.pendown()

t.forward(60)
t.penup()
t.right(180)
t.forward(30)
t.left(90)
t.pendown()
t.forward(40)

t.circle(-30, 100)


turtle.done()
