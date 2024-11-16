from turtle import Screen
from snakee import Snakes
from foode import Food
from scoreb import Scores
scr=Scores()
import time
sc=Screen()
sc.bgcolor("black")
sc.listen()
sc.setup(width=800,height=600)
sc.tracer(0)
s=Snakes()
f=Food()
sc.onkeypress(s.left,"Left")
sc.onkeypress(s.right,"Right")
sc.onkeypress(s.up,"Up")
sc.onkeypress(s.down,"Down")
game_on=True
while game_on:
    time.sleep(0.1)
    s.move()
    sc.update()
    if s.wholesnake[0].distance(f)<=25:
        f.createfood()
        scr.increase_score()
        s.grow()
    if s.check():
        scr.gameover()
        game_on=False
sc.exitonclick()