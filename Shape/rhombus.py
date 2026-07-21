import turtle 

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(90)  
t.pendown()

t.right(50)
t.forward(100)
t.right(88)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.penup()
t.forward(1000)

turtle.done()