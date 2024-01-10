from turtle import Turtle
from random import randint
from math import sqrt

class Food:
    
    def __init__(self, width, height) -> None:
        self.init_board(width, height)
    
    def init_board(self, width, height):
        """ Assign width and height of board for turtles

        Args:
            width (_int_): Width of board, a little bit smaller then width of window
            height (_int_): Height of board, a little bit smaller then height of window
        """
        w = width // 21
        h = height // 21
        self.min_x = -(w // 2)
        self.max_x = w // 2
        self.min_y = -(h // 2)
        self.max_y = h // 2
        self.init_food()
        
    def init_food(self):
        """ Initiaties turtle for drawning food on the screen
        """
        t = Turtle("square", visible = False)
        t.up()
        t.speed(0)
        t.color("red")
        self.food = t
    
    def is_occupied(self, x, y, exc):
        """Checks if coordinates are occupied by a snake

        Args:
            x (_int_): x coordinate
            y (_int_): y coordinate
            exc (_type_): List of occupied coordinates in tuplets like [(1, 1), (1, 2)]

        Returns:
            _bool_: True if x, y coordinates are occupied and False if they are not occupied
        """
        for point in exc:
            px, py = point
            if sqrt((px - x) ** 2 + (py - y) ** 2) < 1:
                return True
        return False
            
    
    def give_food(self, exc):
        """Generate new random position and shows food on Screen

        Args:
            exc (_list_): List of occupied coordinates in tuplets like [(1, 1), (1, 2)]
        """
        while True:
            x = randint(self.min_x, self.max_x) * 21
            y = randint(self.min_y, self.max_y) * 21
            if not self.is_occupied(x, y, exc):
                break
        self.food.goto(x, y)
        self.food.showturtle()
    
    def eat_food(self):
        """Hides turtle object for food when it's eaten
        """
        self.food.hideturtle()
        
    def get_food_coords(self):
        """Gets food coordinates

        Returns:
            _tuple_: Tuple of coorinates where food if located
        """
        return self.food.pos()
    
    def get_food(self):
        """Gets food Turtle object

        Returns:
            _Turtle_: food Turtle object
        """
        return self.food