from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import ScoreBoard
from border import Border

MOVE_SPEED = 0.13

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
scoreboard.increase_score()
border = Border()


# key bindings
screen.listen()
key_map = {
    "Up" : snake.up,
    "w" : snake.up,
    "Down" : snake.down,
    "s" : snake.down,
    "Right" : snake.right,
    "d" : snake.right,
    "Left" : snake.left,
    "a" : snake.left,
}

for key, func in key_map.items():
    screen.onkey(func, key)

# game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(MOVE_SPEED)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tale
    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()