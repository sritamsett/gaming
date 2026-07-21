import turtle 

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 0)
t.setheading(90)   
t.pendown()
t.right(90)
t.forward(30)

t.circle(30, 170)
t.forward(30)
t.circle(-30,170)
t.forward(20)
t.circle(-30,170)
t.forward(30)
t.circle(30,170)

turtle.done()