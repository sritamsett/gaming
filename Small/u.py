import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(270)
t.pendown()

t.forward(30)
t.circle(18,180)
t.forward(30)
t.right(180)
t.forward(40)
t.circle(10,70)
t.penup()
t.forward(50)

turtle.done()