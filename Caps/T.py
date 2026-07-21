import turtle
t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-100, 0)
t.setheading(90)  
t.pendown()
t.forward(150)
t.left(90)
t.penup()
t.forward(50)
t.right(180)
t.pendown()
t.forward(100)

turtle.done()