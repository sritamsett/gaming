import turtle
t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-100, 0)
t.setheading(90)  
t.pendown()

t.forward(90)
t.backward(60)
t.right(45)
t.forward(35)
t.penup()
t.backward(35)
t.right(90)

t.pendown()
t.forward(35)

turtle.done()