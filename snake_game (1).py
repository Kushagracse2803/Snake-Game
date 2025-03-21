'''STEPS TO MAKE A SNAKE GAME'''
#CREATE A SURFACE
#1,CREATE A SNAKE BODY
#2 MOVE THE SNAKE
#3 CREATE SBAKE FOOD
#4 DETECT COLLISION WITH FOOD
#5 CREATE A SCOREBOARD
#6 DETECT COLLISON WITH WALL
#7 DETECT COLLISION WITH TAIL

'''CREATING BOX'''
# from turtle import Screen, Turtle

# Screen=Screen()
# Screen.setup(width=600,height=600)
# Screen.bgcolor("black")
# Screen.title("My Snake Game")
# Screen.exitonclick()

'''CREATE A A SNAKE BODY'''
from turtle import Screen, Turtle
import time

Screen=Screen()
Screen.setup(width=600,height=600)
Screen.bgcolor("black")
Screen.title("My Snake Game")
Screen.tracer(1)

# segment_1=Turtle("square")  
# segment_1.color("white")

# segment_2=Turtle("square")  
# segment_2.color("white")
# segment_2.goto(-20,0)

# segment_3=Turtle("square")  
# segment_3.color("white")
# segment_3.goto(-40,0)

staring_position=[(0,0),(-20,0),(-40,0)]
segments=[]
for position in staring_position:
    new_segment=Turtle("square")
    new_segment.color("white")
    new_segment.penup() #In Python's turtle graphics, the penup() method is used to lift the turtle's pen off 
    #the drawing surface, so that it moves without drawing a line
    new_segment.goto(position)
    segments.append(new_segment)
game_is_on=True
while game_is_on:
    Screen.update()  
    time.sleep(0.1)
    for seg in segments:
      seg.forward(20)
     

Screen.exitonclick()
