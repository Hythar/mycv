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
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
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
    "Handle collision with food."
    print('Snake:', len(snake))
    food.x = randrange(-15, 15) * GRID_SIZE
    food.y = randrange(-15, 15) * GRID_SIZE

def update_board():
    "Update the game board."
    clear()

    for body in snake:
        square(body.x, body.y, GRID_SIZE, 'black')

    square(food.x, food.y, GRID_SIZE, 'green')
    update()

def game_over():
    "Display game over message and exit."
    square(snake[-1].x, snake[-1].y, GRID_SIZE, 'red')
    update()
    bye()

# Set up the game window
setup(420, 420, 370, 0)
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
