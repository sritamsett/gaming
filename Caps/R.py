import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-100, 0)
t.setheading(90)   
t.pendown()

t.forward(150)

t.right(90)
t.circle(-40, 180)
t.left(125)
t.forward(80)


turtle.done()
