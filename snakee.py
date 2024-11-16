from turtle import Turtle,Screen
screen=Screen()
postn=[(0,0),(-20,0),(-40,0)]
class Snakes:
    def __init__(self):
        self.wholesnake=[]
        # self.head=self.wholesnake[0]
        self.create()
    def create(self):
        for pos in postn:
            self.addto(pos)

    def addto(self,posi):
        t=Turtle()
        t.penup()
        t.color("white")
        t.shape("square")

        t.goto(posi)
        self.wholesnake.append(t)

    def check(self):
        for item in self.wholesnake:
            if item.xcor()>380 or item.ycor() > 280 or item.xcor() < -380 or item.ycor() <-280:
                return True
    def grow(self):
        self.addto(self.wholesnake[-1].position())

    def move(self):
        for i in range(len(self.wholesnake)-1,0,-1):
            newx=self.wholesnake[i-1].xcor()
            newy=self.wholesnake[i-1].ycor()
            self.wholesnake[i].goto(newx,newy)
        self.wholesnake[0].forward(20)
    def left(self):
        if self.wholesnake[0].heading()!=0:
            self.wholesnake[0].seth(180)

    def right(self):
        if self.wholesnake[0].heading()!=180:
            self.wholesnake[0].seth(0)
    def up(self):
        if self.wholesnake[0].heading()!=270:
            self.wholesnake[0].seth(90)
    def down(self):
        if self.wholesnake[0].heading()!=90:
            self.wholesnake[0].seth(270)
