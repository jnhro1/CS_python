```jsx
"""
turtleRun2.py
라이브러리 : 도서관, 미리 누군가가 어떤
주제에 관해서 함수를 만들어놓은 것
turtle (거북이, 거북이 게임에 관련된
함수가 미리 저장되어 있다.)

등장인물
- 악당 : devil
- 먹이 : feed
- 주인공거북이 : 따로 이름을 지어주지 않음

함수
1. 가공에 필요한 데이터를 입력받는다.
2. 입력받는 데이터를 가공한다.
3. 가공된 데이터를 내보낸다.
def (define : 정의하다)
def 함수이름(입력값) :
    가공하는 곳
"""
# turtle 라이브러리를 사용하는 방법
import turtle as t
import random

score = 0
isPlay = False

devil = t.Turtle()
devil.shape("turtle")
devil.color("coral1")
devil.speed(0)
devil.up()
devil.goto(0,200)

feed = t.Turtle()
feed.shape("circle")
feed.color("DarkOliveGreen1")
feed.speed(0)
feed.up()
feed.goto(0,-200)

def turn_right() :
    t.setheading(0)

def turn_up() :
    t.setheading(90)
    
def turn_left() :
    t.setheading(180)
    
def turn_down() :
    t.setheading(270)

def start() :
    global isPlay
    if isPlay == False :
        isPlay = True
        t.clear()
        play()

def play():
    global score
    global isPlay
    t.forward(10)
    ang = devil.towards(t.pos())
    devil.setheading(ang)
    devil.forward(8)

    # 먹이를 먹었을 때
    if t.distance(feed) < 12 :
        score = score + 1
        t.write(score)
        feed_x = random.randint(-230, 230)
        feed_y = random.randint(-230, 230)
        feed.goto(feed_x, feed_y)

    # 악당한테 잡혔을 때
    if t.distance(devil) < 12 :
        text = "Score : " + str(score)
        message("Game Over", text)
        isPlay = False
        score = 0
        
    # 게임 지속 조건
    if isPlay :
        t.ontimer(play, 100)

def message(m1, m2) :
    t.clear()
    t.goto(0,100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.setup(500,500)
t.bgcolor("CadetBlue3")
t.shape("turtle")
t.color("DarkSlateBlue")
t.speed(0)
t.up()

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]")
```