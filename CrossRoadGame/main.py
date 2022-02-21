import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
    
    
    if player.is_finish_line():
        scoreboard.update_level()
        player.reset_position()
        car_manager.speed_up()
        

screen.exitonclick()