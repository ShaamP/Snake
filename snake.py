import turtle
import time
import random


delay = 0.075

#Set the screen

window = turtle.Screen()
window.title("Snake By Shaam")
window.bgcolor("green")
window.setup(width = 600, height = 600)
window.tracer(0) #Turns off the screen updates

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier",24,"normal"))

score = 0
high_score = 0

#Functions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction =="down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction =="left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction =="right":
        x = head.xcor()
        head.setx(x+20)

#Keyboard Binding

window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_right, "d")
window.onkeypress(go_left, "a")


#Main game loop
while True:
    window.update()

    #Check for border collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        score = 0
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        delay = 0.1
        #remove segments on new game
        for i in segments:
            i.goto(1000,1000)

        segments.clear()

    #Check Food collision
    if head.distance(food) < 20:
        #Move food to random spot because snake has eaten food
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #move the end segments first in reverse
    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    #check for body collisions
    for i in segments:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            pen.clear()
            score = 0
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            delay = 0.1
            for x in segments:
                x.goto(1000,1000)

            segments.clear()

    time.sleep(delay)




window.mainloop()
