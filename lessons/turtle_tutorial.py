"""Drawing Turtle lesson."""


from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
sidelength: int = 300

colormode(255)
leo.color(99, 204, 250)
leo.penup()
leo.goto(45,60)
leo.pendown()

leo.speed(50)
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(sidelength)
    leo.left(120)
    i = i + 1
leo.end_fill()
leo.hideturtle()
done()

bob: Turtle = Turtle()
bob.color("black")
bob.penup()
bob.goto(45,60)
bob.pendown()

bob.speed(50)
i: int = 0
while i < 4:
    sidelength = sidelength * 0.97
    bob.forward(sidelength)
    bob.left(120)
    i += 1
