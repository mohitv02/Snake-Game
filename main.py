from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My fucking game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
scoreboard = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
screen.update()

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.clean()
        scoreboard.increase_score()
        snake.extent()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for segments in snake.segment:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
