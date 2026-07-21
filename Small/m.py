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
t.backward(40)
t.right(180)
t.circle(-15,180)
t.forward(40)
t.backward(40)
t.right(180)
t.circle(-15,180)
t.forward(40)

turtle.done()