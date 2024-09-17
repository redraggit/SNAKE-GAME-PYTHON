import random
import turtle
import time


delay = 0
score = 0
high_score = 0


wn = turtle.Screen()
wn.bgcolor = ("green")
wn.title = ("snake game")
#height and width
wn.setup(height =600, width =600)
#disable window resize
wn.cv._rootwindow.resizable (False, False)
#delay for update
wn.tracer(0)

#setup for turtlehead
head = turtle.Turtle()

wn.head.color("white")
wn.head.penup() #stop drawing line when moving
wn.head.speed(0)
wn.head.shape("square")
wn.head.goto(0, 0)
wn.head.direction = "stop"

#create the food

shape = random.choice("square, circle")
color = random.choice("white, purple")

food = turtle.Turtle
wn.food.color("color")
wn.food.shape(shape)
wn.food.goto(0, 100) # 0 in width 100 in height
wn.food.penup()

#make the screen score and high score
pen = turtle.Turtle()
pen.color("bleu")
pen.shape("square")
pen.penup()
pen.goto(0)
pen.hideturtle()
pen.write("score=0 high_score=0", align="center", font=("arial, 27, bold"))


#make the direction


def goup():
    if head != "down":
       head = "up"

def godown():
    if head != "up":
        head= "down"
    
def goright():
    if head != "left":
        head = "right"
        
def goleft():
    if head != "right":
        head = "left"
        
        
#make the snake move of direction
def move(): 
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20) #20 pixel
        
    if head.direction == "down":
        y =head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
        
    if head.direction == "right":
        x =head.xcor()
        head.setx(x+20)
        
        
#make the keys button

wn.listen()
wn.onkeypress (goup, "w")
wn.onkeypress (godown, "s")
wn.onkeypress (goleft, "a")
wn.onkeypress (goright, "d")

#checking if head collisions with bords
if (
      head.xcor > 250
  or  head.xcor < -250
  or  head.ycor > 250
  or  head.ycor < -250  
    
):
    
    time.sleep(1)
    head.goto()
    head.direction("stop")
    shapes = random.choice(["circle, square"])
    colors = random.choice(["yellow, purple"])
    food.color = colors
    food.shape = shapes
     
    segments = turtle.Turtle()
    for segment in segments:
         segment.goto(1000, 1000) 
         
    segment.clear()
    
    score = 0
    delay = 0.1
    pen.clear()
    pen.write (
        "score={} high_score={}", format =(score, high_score),  align="center", font="arial, 27, bold"

    )
    
    
    #checking if head hit the wall
    if head.distance(food) < 20:
        x = random.randint(270, -270)
        y = random.randint(270, -270)
        food.goto(x,y)
        
    #adding new segment
    new_segment = turtle.Turtle()
    new_segment.color("yellow") #tail color
    new_segment.shape("square")
    new_segment.penup()
    new_segment.speed(0)
    segment.append(new_segment)
    score += 10 
    delay -= 0.001 #increase speed
    
    if score > high_score :
        score = high_score
    pen.clear()    
    pen.write(
        "score={}, high_score={}", format=(score, high_score), align="center", font="arial, 27, bold"
    )
    #shifting all the snake body(sigments) then move the head
    
    for index in range(len(segments) -1, 0, - 1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
        if len(segments) > 0 : 
          x = head.xcor()
          y = head.ycor() 
        segments[0].goto(x, y)
        
    #cheking if head collisions in body parts
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto()
            head.direction()
            colors=random.choice("white, purple")
            shapes=random.choice("square, circle") 
            food.shape = shapes
            food.color = colors
            
    for segment in segments:
        segment.goto(1000, 1000) 
        segments.clear()
        score = 0
        
        delay = 0.1
        
        pen.clear()
        pen.write(
            "score={}, high_score={}", format=(score, high_score), align="center", font="arial, 27, bold"
         )
    time.sleep(delay)
        