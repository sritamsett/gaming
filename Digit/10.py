import turtle
t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-100, 100)
t.setheading(90)  
t.pendown()

#1
t.right(60)
t.forward(40)

t.right(120)
t.forward(120)
t.left(90)
t.penup()
t.forward(30)
t.right(180)
t.pendown()
t.forward(60)


t.right(180)
t.penup()
t.forward(80)
t.left(90)
t.forward(35)
t.pendown()


#0
t.forward(50)
t.circle(-30, 180)
t.forward(50)
t.circle(-30, 180)


turtle.done()