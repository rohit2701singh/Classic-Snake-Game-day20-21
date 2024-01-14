from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)    # -x: -300, x: 300
screen.bgcolor("black")
screen.title("My Snake Game")
# use tracer and screen update
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # random food generation, eating food, increasing length and increasing score.
    # head means first segment of snake.
    if snake.head.distance(food) < 15:  # distance() turtle method calculates distance between turtle and target point
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # collision with the wall.
    if snake.head.xcor() > 285 or snake.head.xcor() < -299 or snake.head.ycor() > 298 or snake.head.ycor() < -295:
        # game_is_on = False    # if uncommented, game stops after collision
        scoreboard.restart_game()
        snake.snake_reset()

    # collision with tail.
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.restart_game()
            snake.snake_reset()

screen.exitonclick()
