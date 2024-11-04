import turtle


def triangle(position):
    triangle = turtle.Turtle()
    triangle.penup()
    triangle.speed(5)
    triangle.setpos(position)
    triangle.pendown()
    triangle.pensize(10)

    triangle.fd(100)
    triangle.rt(120)
    triangle.fd(100)
    triangle.rt(120)
    triangle.fd(100)


triangle((100, 100))


def square(position):
    square = turtle.Turtle()
    square.penup()
    square.speed(5)
    square.setpos(position)
    square.pendown()
    square.pensize(70)
    square.fd(100)
    square.rt(90)
    square.fd(100)
    square.rt(90)
    square.fd(100)
    square.rt(90)
    square.fd(100)
    square.rt(90)


square((-100. - 100))
