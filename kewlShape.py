from turtle import*

speed(0)
shape('arrow')



wn=Screen()
wn.bgcolor('light green')


x=0
up()

rt(45)
fd(90)
rt(135)


down()

while x < 240:
  fd(75)
  color('yellow')
  lt(676)

  fd(190)
  color('orange red')
  lt(150)

  fd(137)
  color('red')

  rt(11.111)
  x = x+ 1.1