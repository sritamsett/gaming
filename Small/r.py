import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(270)
t.pendown()
t.forward(100)
t.right(180)
t.forward(60)
t.circle(-30,120)

turtle.done()