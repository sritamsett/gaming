import turtle 

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(90)  
t.pendown()

t.right(90)
t.forward(85)
t.left(75)
t.forward(80)
t.left(70)
t.forward(80)
t.left(70)
t.forward(80)
t.left(70)
t.forward(80)

t.penup()
t.forward(1000)

turtle.done()