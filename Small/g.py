import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(90)
t.pendown()

t.left(90)

t.forward(40)
t.circle(-30, 180)
t.forward(40)
t.left(90)
t.forward(5)
t.right(180)
t.forward(100)
t.circle(-30, 60)
t.right(30)
t.forward(35)
t.circle(-20,90)


turtle.done()
