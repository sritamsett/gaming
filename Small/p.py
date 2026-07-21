import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 0)
t.setheading(90)
t.pendown()

t.forward(90)
t.right(180)
t.penup()
t.forward(75)
t.right(180)
t.forward(5)
t.right(90)
t.pendown()

t.forward(40)
t.circle(30, 180)

t.forward(40)
t.penup()
t.left(90)
t.forward(70)
t.pendown()
t.forward(50)

turtle.done()
