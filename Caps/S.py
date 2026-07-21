import turtle 

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 0)
t.setheading(90)   # face left
t.pendown()
t.right(90)
t.forward(40)

t.circle(20, 170)
t.forward(30)
t.circle(-20,170)
t.forward(40)



turtle.done()