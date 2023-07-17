import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()                  # create a scoreboard
# Move the turtle with key press
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

# Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


# Detect successful crossing (when turtle reaches the other side)
    if player.is_at_finish_line():          # if is_at_finish method is true, then call go_to_start
        player.go_to_start()
        car_manager.level_up()              # car speed increases after level by level.
        scoreboard.increase_level()

screen.exitonclick()
