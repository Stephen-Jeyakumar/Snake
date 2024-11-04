import turtle

window = turtle.Screen()

window.bgcolor("lightgreen")

turtle = turtle.Turtle()

turtle.color("blue")
turtle.pensize(3)
turtle.shape('circle')


sides = str(input("How many sides do you want? Use digits: "))

length = turtle.fd(50)

def polygon(sides,length):
  for x in (sides):
    turtle.forward(length)
    turtle.left(360/sides)

polygon(sides, length)

