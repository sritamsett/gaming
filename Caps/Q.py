import turtle
t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-100, 0)
t.setheading(90)  
t.pendown()

t.circle(-75,360)
t.penup()
t.right(180)
t.circle(75,140)
t.left(90)
t.forward(20)
t.right(180)
t.pendown()
t.forward(60)

turtle.done()