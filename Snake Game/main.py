import turtle
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard


# set the speed of the game
GAME_SPEED = 7
# dimensions for the game window
WIDTH = 800
HEIGHT = 600

# convert the game speed to milliseconds
wait_time = (11 - GAME_SPEED) / 30
# calculate the borders
x_range = int(WIDTH / 2) - 10
y_range = int(HEIGHT / 2) - 10


# screen setup
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Snake game")
screen.bgcolor("white")
# disable automatic screen updates
screen.tracer(0)

# snake setup
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# controls setup
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_over = False
while not game_is_over:
    # update the screen
    screen.update()
    # to control the speed
    time.sleep(wait_time)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 10:
        scoreboard.add_one()
        snake.extend()
        food.respawn()

    # detect collision with wall
    if snake.head.xcor() < -x_range or snake.head.xcor() > x_range \
            or snake.head.ycor() < -y_range or snake.head.ycor() > y_range:
        game_is_over = True

    # detect collision with tail
    for i in range(1, snake.length):
        if snake.head.distance(snake.segments[i]) < 10:
            game_is_over = True

# display the game over message
scoreboard.game_over()

# wait for click before closing the window
screen.exitonclick()