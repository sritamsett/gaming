import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(0, 100)
t.setheading(90)   
t.pendown()

t.left(90)
t.forward(70)
t.left(90)
t.forward(40)
t.left(90)
t.forward(30)
t.circle(-35, 180)
t.forward(30)


turtle.done()
