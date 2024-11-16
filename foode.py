import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.createfood()
    def createfood(self):
        self.clear()
        self.color("green")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.shape("circle")
        x=random.randint(-380,380)
        y=random.randint(-280,280)
        self.penup()
        self.goto(x,y)
    # def __init__(self):
    #     self.createfood()
    # def createfood(self):
    #     t=Turtle()
    #     t.clear()
    #     t.color("blue")
    #     t.shapesize(0.5,0.5)
    #     x=random.randint(-380,380)
    #     y=random.randint(-280,280)
    #     t.shape("turtle")
    #     t.penup()
    #     t.goto(x,y)
