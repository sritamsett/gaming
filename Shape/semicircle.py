import turtle 

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, 50)
t.setheading(90)  
t.pendown()

t.right(90)
t.forward(200)
t.left(90)
t.circle(100,180)

turtle.done()