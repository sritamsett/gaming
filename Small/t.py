import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(270)
t.pendown()

t.forward(30)
t.left(90)
t.penup()
t.forward(20)
t.right(180)
t.pendown()
t.forward(40)
t.penup()
t.right(180)
t.forward(20)
t.right(90)
t.pendown()
t.forward(60)
t.circle(18,160)


turtle.done()