import turtle
t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-100, 100)
t.setheading(90)  
t.pendown()

t.right(90)
t.forward(10)

t.right(90)
t.forward(50)
t.left(90)
t.penup()
t.forward(10)
t.right(180)
t.pendown()
t.forward(20)
t.right(180)
t.penup()
t.forward(10)
t.left(90)
t.forward(65)
t.pendown()
t.circle(2,360)
t.penup()
t.forward(120)

turtle.done()