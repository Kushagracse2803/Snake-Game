from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier",24,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        # self.high_score=0   #whenever you start a game it will reset your hight score
        #to avoid this we will use files.txt filereading concept to avoid this
        with open("DAY20/data.txt") as data:
          self.high_score= int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}",align=ALIGNMENT,font=FONT)
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("HAAR GAYE",align=ALIGNMENT,font=FONT)
    def reset(self):
       if self.score >self.high_score:
          self.high_score=self.score
          with open("DAY20/data.txt",mode="w") as data:
             data.write(f"{self.high_score}")
       self.score=0
       self.update_scoreboard()
    
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
