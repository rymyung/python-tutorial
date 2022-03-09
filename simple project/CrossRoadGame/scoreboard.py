from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.level = 0
        self.update_level()


    def update_level(self): 
        self.level += 1
        self.clear()
        self.goto(-200, 250)
        self.write(f'LEVEL : {self.level}', align='center', font=FONT)
    
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=FONT)