import turtle 

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(90)  
t.pendown()

t.right(90)
t.forward(150)
t.left(60)
t.forward(70)
t.left(120)
t.forward(150)
t.left(60)
t.forward(70)

t.penup()
t.forward(1000)

turtle.done()