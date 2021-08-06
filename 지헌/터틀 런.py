import turtle as t
import random as r

score = 0
playing = False
#악마
devil = t.Turtle()
devil.shape("arrow")
devil.color("red")
devil.speed(0)
devil.up()
devil.goto(0,200)
#먹이
feed = t.Turtle()
feed.shape("turtle")
feed.color("green")
feed.speed(0)
feed.up()
feed.goto(0,-200)
#이동
def turn_right():
  t.setheading(0)
def turn_left():
  t.setheading(180)
def turn_up():
  t.setheading(90)
def turn_down():
  t.setheading(270)
  #시작
def start():
  global playing
  if playing == False:
    playing = True
    t.clear()
    play()
def play():
  global score
  global playing
  t.forward(10)
  if r.randint(1,5) == 3:
    ang = devil.towards(t.pos())
    devil.setheading(ang)
  speed = score + 5

  if speed > 15:
    speed = 15
  devil.forward(speed)
# 게임이 끝나는 조건
  if t.distance(devil) < 12:
    text = "Score : " + str(score)
    message("Game Over", text)
    playing = False
    score = 0
#거북이가 먹이를 먹었을때
  if t.distance(feed) < 12:
    score += 1
    t.write(score)
    star_x = r.randint(-230,230)
    star_y = r.randint(-230,230)
    feed.goto(star_x,star_y)

  if playing:
    t.ontimer(play, 100)

def message(m1,m2):
  t.clear()
  t.goto(0,100)
  t.write(m1,False, "center", ("",20))
  t.goto(0, -100)
  t.write(m2, False, "center", ("", 15))
  t.home()

t.title("Turtle Run")
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
t.onkeypress(start, "space")
t.listen()
message("Trutle Run", "[Press space]")






    
    
    
    
    


