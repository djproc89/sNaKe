from turtle import Screen
from Snake import Snake
from Food import Food

# screen size
width = 840
height = 630

# screen setup
s = Screen()
s.title("sNaKe")
s.screensize(width + 24, height + 24)
s.setup(width + 32, height + 32)

# objects for Snake and Food classes
snake = Snake(width, height)
food = Food(width, height)

# binds keys
s.listen()
s.onkey(lambda: snake.set_direction(0), "Right")
s.onkey(lambda: snake.set_direction(180), "Left")
s.onkey(lambda: snake.set_direction(90), "Up")
s.onkey(lambda: snake.set_direction(270), "Down")
s.onkey(lambda: s.delay(snake.increase_lvl()), "KP_Add")
# s.onkey(lambda: s.delay(snake.decrease_lvl()), "-")
# s.onkey(snake.expand_body, "q")
# s.onkey(snake.move, "space")

# shows first food on screen
food.give_food(snake.get_coords())
# moves snake
while snake.alive:
    s.delay(snake.get_delay())
    snake.move()
    if food.get_food().distance(snake.get_head()) < 1:
        snake.eat()
        food.eat_food()
        food.give_food(snake.get_coords())
s.textinput(f"You loose! Your score is: {snake.score}", None)
