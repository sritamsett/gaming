import turtle 

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(90)  
t.pendown()

t.right(60)
t.forward(60)
t.right(70)
t.forward(60)
t.right(75)
t.forward(120)
t.right(132)
t.forward(125)
t.penup()
t.forward(1000)

turtle.done()