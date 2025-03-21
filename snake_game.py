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


# segment_1=Turtle("square")  
# segment_1.color("white")

# segment_2=Turtle("square")  
# segment_2.color("white")
# segment_2.goto(-20,0)

# segment_3=Turtle("square")  
# segment_3.color("white")
# segment_3.goto(-40,0)
'''CREATE A A SNAKE BODY'''

# from turtle import Screen, Turtle
# import time

# Screen=Screen()
# Screen.setup(width=600,height=600)
# Screen.bgcolor("black")
# Screen.title("My Snake Game")
# Screen.tracer(0)

# staring_position=[(0,0),(-20,0),(-40,0)]
# segments=[]
# for position in staring_position:
#     new_segment=Turtle("square")
#     new_segment.color("white")
#     new_segment.penup() #In Python's turtle graphics, the penup() method is used to lift the turtle's pen off 
#     #the drawing surface, so that it moves without drawing a line
#     new_segment.goto(position)
    # segments.append(new_segment)
# game_is_on=True
# while game_is_on:
#     Screen.update()  
#     time.sleep(0.1)
#     for seg in segments:
#       seg.forward(20)
     

# Screen.exitonclick()
'''MOVING A SNAKE AT A SPECIFIC PATH LEFT RIGHT UP OR DOWN'''
'''CREATE A A SNAKE BODY'''

# from turtle import Screen, Turtle
# import time

# Screen=Screen()
# Screen.setup(width=600,height=600)
# Screen.bgcolor("black")
# Screen.title("My Snake Game")
# Screen.tracer(0)

# staring_position=[(0,0),(-20,0),(-40,0)]
# segments=[]
# for position in staring_position:
#     new_segment=Turtle("square")
#     new_segment.color("white")
#     new_segment.penup() #In Python's turtle graphics, the penup() method is used to lift the turtle's pen off 
#     #the drawing surface, so that it moves without drawing a line
#     new_segment.goto(position)
#     segments.append(new_segment)
# game_is_on=True
'''In this code block:

The while game_is_on: loop runs the game continuously as long as game_is_on is True.
Screen.update() refreshes the screen with each iteration, and time.sleep(0.1) pauses the loop briefly to slow down the snake’s movement.
The for loop (for seg_num in range(len(segments)-1, 0, -1):) moves each segment of the snake starting from the tail (last segment) to follow the segment ahead of it.
For each segment seg_num, the coordinates (xcor, ycor) of the segment just before it (seg_num-1) are retrieved and assigned to the current segment (seg_num), making it move to the previous segment's position.
The first segment (segments[0], the snake's head) moves forward by 20 units, making the snake appear to slither.
This replicates the snake's movement by shifting all segments forward in sequence.'''
# while game_is_on:
#     Screen.update()  
#     time.sleep(0.1)
#     # for seg_num in range(start=2,stop=0,step=-1):#moving snake from block 2 to 1 the 1 to 0
    # for seg_num in range(len(segments)-1,0,-1):
    #   new_x=segments[seg_num-1].xcor()
    #   new_y=segments[seg_num-1].ycor()
    #   segments[seg_num].goto(new_x,new_y)
    # segments[0].forward(20)

'''new_x=segments[seg_num-1].xcor():

This line gets the x-coordinate (xcor()) of the segment immediately in front of the current segment (segments[seg_num-1]).
segments is likely a list (or an array) of objects representing the body parts of the snake, where each part (segment) has a position (xcor() returns the x-coordinate of that position).
seg_num is the index of the current segment being processed in the loop. By subtracting 1, you're referencing the segment directly in front of the current one.
new_y=segments[seg_num-1].ycor():

This line is similar to the first, but it gets the y-coordinate (ycor()) of the segment directly in front of the current one.
segments[seg_num].goto(new_x,new_y):

This line moves the current segment (segments[seg_num]) to the position (new_x, new_y) obtained from the segment ahead of it.
goto() is likely a method that updates the position of an object by moving it to the specified coordinates.'''


#TILL NOW WE CREATED THE SNAKE AND MOVE THE SNAKE NOW
#WE WILL MAKW THREE CLASS 1,SNAKE 2,FOOD 3,SCOREBOARD


# from turtle import Screen, Turtle
# import time

# Screen=Screen()
# Screen.setup(width=600,height=600)
# Screen.bgcolor("black")
# Screen.title("My Snake Game")
# Screen.tracer(0)

# staring_position=[(0,0),(-20,0),(-40,0)]
# segments=[]


# for position in staring_position:
#     new_segment=Turtle("square")
#     new_segment.color("white")
#     new_segment.penup() #In Python's turtle graphics, the penup() method is used to lift the turtle's pen off 
#     #the drawing surface, so that it moves without drawing a line
#     new_segment.goto(position)
#     segments.append(new_segment)
# game_is_on=True
# while game_is_on:
#     Screen.update()  
#     time.sleep(0.1)
#     # for seg_num in range(start=2,stop=0,step=-1):#moving snake from block 2 to 1 the 1 to 0
#     for seg_num in range(len(segments)-1,0,-1):
#       new_x=segments[seg_num-1].xcor()
#       new_y=segments[seg_num-1].ycor()
#       segments[seg_num].goto(new_x,new_y)
#     segments[0].forward(20)
'''USING CLASSES AND OBJECT'''


# from turtle import Screen, Turtle
# from snake import Snake

# import time

# screen=Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
# snake=Snake()
# '''Screen.listen()
# The listen() method in the Turtle module allows the program to listen for keyboard or mouse events. This means it starts waiting for key presses so that you can bind certain keys to specific functions or actions.'''
# screen.listen()
# screen.onkey(snake.up,"Up")
# screen.onkey(snake.down,"Down")
# screen.onkey(snake.left,"Left")
# screen.onkey(snake.right,"Right")

# game_is_on=True
# while game_is_on:
#     screen.update()  
#     time.sleep(0.1)
#     snake.move()
# screen.exitonclick()

'''DAY 21--> INHERITANCE -->INHERIT THE PROPERRTY FROM PARENTS CLASS'''
 #SUPER KEYWORD
'''In Python, a super keyword is used to call methods from a parent class. It allows you to access inherited methods and properties without explicitly naming the parent class. This is particularly useful in class inheritance 
 and can help avoid issues related to multiple inheritance.'''



#DETECT COLLISION WITH FOOD

# from turtle import Screen, Turtle
# from snake import Snake
# from food import Food

# import time

# screen=Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
# snake=Snake()
# food=Food()
# '''Screen.listen()
# The listen() method in the Turtle module allows the program to listen for keyboard or mouse events. This means it starts waiting for key presses so that you can bind certain keys to specific functions or actions.'''
# screen.listen()
# screen.onkey(snake.up,"Up")
# screen.onkey(snake.down,"Down")
# screen.onkey(snake.left,"Left")
# screen.onkey(snake.right,"Right")

# game_is_on=True
# while game_is_on:
#     screen.update()  
#     time.sleep(0.1)
#     snake.move()
#     '''In Python's turtle graphics library, the .distance() method is used to calculate the distance between
#       the turtle's current position and a specified point (given by coordinates). This can be useful for determining how far 
#     the turtle is from a specific location without moving it.'''
#     if snake.head.distance(food)<15:
#         food.refresh()
# screen.exitonclick()

'''CREATING A SCORE BOARD'''
# from turtle import Screen, Turtle
# from snake import Snake
# from food import Food
# from score import Scoreboard

# import time

# screen=Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
# snake=Snake()
# food=Food()
# scoreboard=Scoreboard()
# '''Screen.listen()
# The listen() method in the Turtle module allows the program to listen for keyboard or mouse events. This means it starts waiting for key presses so that you can bind certain keys to specific functions or actions.'''
# screen.listen()
# screen.onkey(snake.up,"Up")
# screen.onkey(snake.down,"Down")
# screen.onkey(snake.left,"Left")
# screen.onkey(snake.right,"Right")

# game_is_on=True
# while game_is_on:
#     screen.update()  
#     time.sleep(0.1)
#     snake.move()
#     '''In Python's turtle graphics library, the .distance() method is used to calculate the distance between
#       the turtle's current position and a specified point (given by coordinates). This can be useful for determining how far 
#     the turtle is from a specific location without moving it.'''
#     if snake.head.distance(food)<15:
#         food.refresh()
#         scoreboard.increase_score()
# screen.exitonclick()
 
# '''detect collision with wall'''
# from turtle import Screen, Turtle
# from snake import Snake
# from food import Food
# from score import Scoreboard

# import time

# screen=Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
# snake=Snake()
# food=Food()
# scoreboard=Scoreboard()
# '''Screen.listen()
# The listen() method in the Turtle module allows the program to listen for keyboard or mouse events. This means it starts waiting for key presses so that you can bind certain keys to specific functions or actions.'''
# screen.listen()
# screen.onkey(snake.up,"Up")
# screen.onkey(snake.down,"Down")
# screen.onkey(snake.left,"Left")
# screen.onkey(snake.right,"Right")

# game_is_on=True
# while game_is_on:
#     screen.update()  
#     time.sleep(0.1)
#     snake.move()
#     '''In Python's turtle graphics library, the .distance() method is used to calculate the distance between
#       the turtle's current position and a specified point (given by coordinates). This can be useful for determining how far 
#     the turtle is from a specific location without moving it.'''
#     if snake.head.distance(food)<15:
#         food.refresh()
#         scoreboard.increase_score()
#     #DETECT COLLISON WITH WALL
#     if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
#         game_is_on=False
#         scoreboard.game_over()
# screen.exitonclick()
'''detect collision with tail'''
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Scoreboard

import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()
'''Screen.listen()
The listen() method in the Turtle module allows the program to listen for keyboard or mouse events. This means it starts waiting for key presses so that you can bind certain keys to specific functions or actions.'''
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()  
    time.sleep(0.1)
    snake.move()
    '''In Python's turtle graphics library, the .distance() method is used to calculate the distance between
      the turtle's current position and a specified point (given by coordinates). This can be useful for determining how far 
    the turtle is from a specific location without moving it.'''
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #DETECT COLLISON WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        # game_is_on=False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset() 
    #DETECT COLLISON WITH TAIL.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<  10:
            # game_is_on=False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
    
    #IF HEAD COLLIDES WITH ANY SEGMENT IN THE TAIL :
     #TRIGGER GAME_OVER



screen.exitonclick()
 