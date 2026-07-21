import turtle
t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-100, 0)
t.setheading(90)  
t.pendown()

t.right(90)
t.forward(10)
t.right(90)
t.forward(50)

t.circle(5, 110)
t.penup()
t.forward(50)

turtle.done()