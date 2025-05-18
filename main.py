import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

gamer = Player()
car_manager = CarManager()
score = Scoreboard()
score.update_scoreboard()

screen.listen()
screen.onkeypress(gamer.move_up, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    # Detect the collision 
    for car in car_manager.all_cars:
        if car.distance(gamer) < 20:
            game_is_on =False
            score.game_over()

    # Detect successfull crossing 
    if gamer.is_at_finish_line():
        gamer.got_to_start()
        car_manager.level_up()
        score.increase_level()
    

screen.exitonclick()