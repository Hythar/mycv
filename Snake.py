from turtle import *
from random import randrange
from freegames import square, vector

# Constants
GRID_SIZE = 20
MOVE_INTERVAL = 100

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -GRID_SIZE)

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        game_over()
        return

    snake.append(head)

    if head == food:
        handle_food_collision()
    else:
        snake.pop(0)

    update_board()
    ontimer(move, MOVE_INTERVAL)

def handle_food_collision():
   
    print('Snake:', len(snake))
    food.x = randrange(-15, 15) * GRID_SIZE
    food.y = randrange(-15, 15) * GRID_SIZE

def update_board():
    clear()

    # Draw grid lines
    for x in range(-200, 200, GRID_SIZE):
        square(x, -200, 1, 'gray')
        square(x, 200, 1, 'gray')

    for y in range(-200, 200, GRID_SIZE):
        square(-200, y, 1, 'gray')
        square(200, y, 1, 'gray')

    # Draw snake
    for body in snake:
        square(body.x, body.y, GRID_SIZE, 'black')

    # Draw food
    square(food.x, food.y, GRID_SIZE, 'green')
    update()

def game_over():
    
    square(snake[-1].x, snake[-1].y, GRID_SIZE, 'red')
    update()
    bye()

# Set up the game window
setup(420, 420, 370, 0)
title("Snake Game")
bgcolor("lightblue")

hideturtle()
tracer(False)
listen()

# Set up key bindings
onkey(lambda: change(GRID_SIZE, 0), 'Right')
onkey(lambda: change(-GRID_SIZE, 0), 'Left')
onkey(lambda: change(0, GRID_SIZE), 'Up')
onkey(lambda: change(0, -GRID_SIZE), 'Down')

# Start the game
move()
done()
