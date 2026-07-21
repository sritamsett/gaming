import turtle 

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-40, 0)
t.setheading(90)  
t.pendown()

t.left(30)
t.circle(-30,180)
t.left(120)
t.circle(-30,180)
t.right(10)
t.forward(80)
t.right(100)
t.forward(80)

t.penup()
t.forward(10000)

turtle.done()