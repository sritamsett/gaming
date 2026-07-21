import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(0, -50)
t.setheading(90)   
t.pendown()

t.forward(100)

t.right(90)
t.circle(-25, 180)

t.penup()
t.goto(0, 0)
t.setheading(0)
t.pendown()


t.circle(-25, 180)

turtle.done()
