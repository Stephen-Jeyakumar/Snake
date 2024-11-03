import turtle
import time
import random



segments = []

# Screen Setup
wn = turtle.Screen()
wn.setup(width=500, height=500)
wn.bgcolor('light green')
wn.tracer(0)

# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('blue')
head.penup()
head.goto(0, 100)
head.direction = 'stop'

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape('turtle')
food.color('dark green')
food.penup()

food.goto(0, 0)

# Scores
score = 0
high_score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('red')
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write('Score: 0 High Score: {}'.format(high_score), align='center', font=('Comic Sans', 22, 'normal'))

def move():
  if head.direction == 'up':
    head.sety(head.ycor() + 20)

  if head.direction == 'down':
    head.sety(head.ycor() - 20)

  if head.direction == 'right':
    head.setx(head.xcor() + 20)

  if head.direction == 'left':
    head.setx(head.xcor() - 20)

def go_up():
  if head.direction != 'down':
    head.direction = 'up'

def go_down():
  if head.direction != 'up':
    head.direction = 'down'

def go_right():
  if head.direction != 'left':
    head.direction = 'right'

def go_left():
  if head.direction != 'right':
    head.direction = 'left'

wn.listen()
wn.onkey(go_up, 'Up')
wn.onkey(go_down, 'Down')
wn.onkey(go_right, 'Right')
wn.onkey(go_left, 'Left')

# Main Game Loop
while True:
  wn.update()

  if head.distance(food) < 15:
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    food.goto(x, y)

    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape('circle')
    new_segment.color('navy' )


    new_segment.penup()
    segments.append(new_segment)

    score = score + 1
    if score > high_score:
      high_score = score

  for i in range(len(segments)-1, 0, -1):
    x = segments[i-1].xcor()
    y = segments[i-1].ycor()
    segments[i].goto(x, y)

  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

  if head.xcor() > 250 or head.xcor() < -250 or head.ycor() > 250 or head.ycor() < -250:
    time.sleep(1)
    head.goto(0, 0)
    head.direction = 'stop'

    for segment in segments:
      segment.hideturtle()

    segments = []
    score = 0

  move()

  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      head.goto(0, 0)
      head.direction = 'stop'

      for segment in segments:
        segment.hideturtle()

      segments = []
      score = 0

  pen.clear()
  pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font=('Courier', 22, 'normal'))

  time.sleep(0.15)