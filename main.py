from turtle import Turtle, Screen
from snake import Snake
from foo import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("brown")
my_screen.title("Snake")
my_screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")
is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.mov()
    # Dectect food collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() > 288 or snake.head.ycor() < -288:
        is_game_on = False
        score.game_over()
my_screen.exitonclick()
