import turtle
t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-100, 100)
t.setheading(90)  
t.pendown()

t.right(90)
t.forward(20)
t.backward(10)
t.left(90)
t.penup()
t.forward(20)
t.pendown()
t.circle(2,360)
t.right(180)
t.penup()
t.forward(22)
t.left(90)
t.forward(10)
t.pendown()
t.right(90)
t.forward(60)
t.circle(-10,160)



turtle.done()