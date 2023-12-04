import turtle
t = turtle.Turtle()
t.shape('turtle')
t.pensize(10 )
t.left(90)
color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
for i in range(7):
    t.color(color[i])
    t.circle(20 *(i+1), 180)
    t.penup()
    t.goto(20*(i+1), 0)
    t.pendown()  
    t.left(180)
turtle.done()

