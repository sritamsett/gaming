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
t.backward(30)
t.left(130)
t.penup()
t.forward(30)
t.right(180)
t.pendown()
t.forward(60)


turtle.done()