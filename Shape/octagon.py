import turtle 

t = turtle.Turtle()
t.speed(3)

t.pensize(6)

t.penup()
t.goto(-40, 0)
t.setheading(90)  
t.pendown()

t.right(90)
t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)

for i in range(0,8):
    t.left(45)
    t.forward(100)

t.penup()
t.forward(1000)

turtle.done()