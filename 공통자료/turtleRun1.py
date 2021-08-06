import turtle as t
import random

devil = t.Turtle()
devil.shape("turtle")
devil.color("red")
devil.speed(0)
devil.up()
devil.goto(0,200)

feed = t.Turtle()
feed.shape("circle")
feed.color("green")
feed.speed(0)
feed.up()
feed.goto(0,-200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def play():
    t.forward(10)
    ang = devil.towards(t.pos())
    devil.setheading(ang)
    devil.forward(9)
    if t.distance(feed) < 12:
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        feed.goto(star_x, star_y)
    if t.distance(devil) >= 12:
        t.ontimer(play, 100)

t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
play()

        
