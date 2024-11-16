from turtle import Turtle
class Scores(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("violet")
        self.penup()
        with open("my.txt") as dat:
            self.highscore=int(dat.read())
        self.hideturtle()
        self.goto(-230,250)
        self.write(f"Score: {self.score} ; HighScore: {self.highscore}",False,"center",("Calibri",20,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} ; HighScore: {self.highscore}",False,"center",("Calibri",20,"normal"))
    def gameover(self):
        self.penup()
        self.hideturtle()
        if self.score>self.highscore:
            self.highscore=self.score
            with open("my.txt", mode="w") as dat:
                dat.write(f"{self.highscore}")
        self.clear()
        self.write(f"Score: {self.score} ; HighScore: {self.highscore}", False, "center", ("Calibri", 23, "normal"))

        self.goto(0,0)
        self.write("GAME OVER",False,"center",("Calibri",48,"normal"))

        