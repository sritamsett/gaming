import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(90)
t.pendown()

t.right(90)
t.forward(40)
t.circle(-30, 100)
t.left(10)
t.forward(70)
t.right(180)
t.penup()
t.forward(5)
t.pendown()

t.left(90)
t.forward(40)
t.circle(-30, 180)
t.forward(35)


turtle.done()
