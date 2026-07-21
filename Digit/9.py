import turtle

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-50, -50)
t.setheading(0)
t.pendown()

t.right(30)
t.circle(60, 200)
t.circle(30, 300)


turtle.done()