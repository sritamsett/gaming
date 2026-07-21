import turtle
t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-100, 100)
t.setheading(90)  
t.pendown()

t.right(60)
t.forward(50)

t.right(120)
t.forward(150)
t.left(90)
t.penup()
t.forward(40)
t.right(180)
t.pendown()
t.forward(80)

turtle.done()