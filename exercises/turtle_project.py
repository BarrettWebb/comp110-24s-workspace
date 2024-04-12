"""UNC bell tower."""
 
__author__ = "730544769"
 
from turtle import Turtle, colormode, done, tracer, update
    

def draw_square(square: Turtle, x: float, y: float, width: float) -> None:
    """Drawing a square in scene."""
    square.pensize(1)
    square.penup()
    square.goto(x, y)
    square.setheading(0.0)
    square.pendown()
    i: int = 0
    while i < 4:
        square.forward(width)
        square.right(90)
        i += 1


def draw_rectangle(rectangle: Turtle, x: float, y: float, width: float, height: float, r: int, g: int, b: int) -> None:
    """Drawing a rectangle in scene."""
    colormode(255)
    rectangle.pensize(1)
    rectangle.penup()
    rectangle.goto(x, y)
    rectangle.setheading(0.0)
    rectangle.pencolor("black")
    rectangle.fillcolor(r, g, b)
    rectangle.pendown()
    i: int = 0
    rectangle.begin_fill()
    while i < 2:
        rectangle.forward(width)
        rectangle.right(90)
        rectangle.forward(height)
        rectangle.right(90)
        i += 1
    rectangle.end_fill()


def draw_circle(circle: Turtle, x: float, y: float, width: float, r: int, g: int, b: int) -> None:
    """Drawing a circle in scene."""
    colormode(255)
    circle.pensize(1)
    circle.penup()
    circle.goto(x, y)
    circle.pencolor("black")
    circle.fillcolor(r, g, b)
    circle.pendown()
    circle.begin_fill()
    circle.circle(width)
    circle.end_fill()


def draw_half_circle(circle: Turtle, x: float, y: float, width: float, r: int, g: int, b: int) -> None:
    """Drawing a half circle in scene."""
    colormode(255)
    circle.pensize(1)
    circle.penup()
    circle.goto(x, y)
    circle.pencolor("black")
    circle.fillcolor(r, g, b)
    circle.setheading(90)
    circle.pendown()
    circle.begin_fill()
    circle.circle(width, 180)
    circle.end_fill()


def draw_arch(arch: Turtle, x: float, y: float, width: float, height: float, r: int, g: int, b: int) -> None:
    """Drawing an arch in scene."""
    colormode(255)
    arch.pensize(1)
    arch.penup()
    arch.goto(x, y)
    arch.pencolor("black")
    arch.fillcolor(r, g, b)
    arch.setheading(270)
    arch.pendown()
    arch.begin_fill()
    arch.forward(height)
    arch.left(90)
    arch.forward(width)
    arch.left(90)
    arch.forward(height)
    arch.circle(width / 2, 180)
    arch.end_fill()
    

def draw_triangle(triangle: Turtle, x: float, y: float, width: float, r: int, g: int, b: int) -> None:
    """Drawing a triangle in scene."""
    colormode(255)
    triangle.pensize(1)
    triangle.penup()
    triangle.goto(x, y)
    triangle.pencolor("black")
    triangle.fillcolor(r, g, b)
    triangle.setheading(0.0)
    triangle.pendown()
    triangle.begin_fill()
    triangle.forward(width)
    triangle.left(120)
    triangle.forward(width)
    triangle.left(120)
    triangle.forward(width)
    triangle.left(120)
    triangle.end_fill()


def draw_line(line: Turtle, x: float, y: float, length: float, angle: float) -> None:
    """Draw line in scene."""
    line.penup()
    line.goto(x, y)
    line.pencolor("black")
    line.pensize(2)
    line.setheading(angle)
    line.pendown()
    line.forward(length)


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    bob: Turtle = Turtle()
    bob.speed(50)
    # draw ground
    draw_rectangle(bob, -300, -200, 600, 200, 76, 153, 0)
    # draw sky
    draw_rectangle(bob, -300, 400, 600, 600, 102, 178, 255)
    # draw base
    draw_rectangle(bob, -75, -100, 150, 100, 153, 102, 51)
    # draw tower
    draw_rectangle(bob, -32.5, 200, 65, 300, 153, 102, 51)
    # draw clock
    draw_circle(bob, 0, 150, 20, 255, 255, 255)
    # draw grey on top of base
    draw_rectangle(bob, -80, -100, 160, 15, 150, 150, 150)
    # pillars on base
    draw_rectangle(bob, -80, -115, 10, 85, 150, 150, 150)
    draw_rectangle(bob, -30, -115, 10, 85, 150, 150, 150)
    draw_rectangle(bob, 20, -115, 10, 85, 150, 150, 150)
    draw_rectangle(bob, 70, -115, 10, 85, 150, 150, 150)
    # arches on base
    draw_arch(bob, 35, -145, 30, 55, 102, 178, 255)
    draw_arch(bob, -15, -145, 30, 55, 102, 178, 255)
    draw_arch(bob, -65, -145, 30, 55, 102, 178, 255)
    # top of tower
    draw_triangle(bob, -25, 295, 51, 181, 181, 181)
    draw_rectangle(bob, -25, 295, 3, 45, 150, 150, 150)
    draw_rectangle(bob, -15, 295, 3, 45, 150, 150, 150)
    draw_rectangle(bob, -5, 295, 3, 45, 150, 150, 150)
    draw_rectangle(bob, 5, 295, 3, 45, 150, 150, 150)
    draw_rectangle(bob, 15, 295, 3, 45, 150, 150, 150)
    draw_rectangle(bob, 23, 295, 3, 45, 150, 150, 150)
    draw_rectangle(bob, -26, 295, 52.5, 3, 150, 150, 150)
    draw_half_circle(bob, 30, 240, 30, 153, 102, 51)
    draw_rectangle(bob, -33, 255, 65.5, 50, 153, 102, 51)
    draw_rectangle(bob, -33, 235, 65.5, 25, 102, 178, 255)
    draw_rectangle(bob, -33, 255, 65.5, 5, 150, 150, 150)
    draw_rectangle(bob, -33, 210, 65.5, 10, 150, 150, 150)
    draw_rectangle(bob, -33, 255, 5, 45, 150, 150, 150)
    draw_rectangle(bob, -17.5, 255, 5, 45, 150, 150, 150)
    draw_rectangle(bob, 12.5, 255, 5, 45, 150, 150, 150)
    draw_rectangle(bob, 28, 255, 5, 45, 150, 150, 150)
    draw_arch(bob, -12.5, 235, 25, 25, 102, 178, 255)
    draw_line(bob, 0, 170, 13, 90)
    draw_line(bob, 0, 170, 17, 300)
    update()
    done()


if __name__ == "__main__":
    main()