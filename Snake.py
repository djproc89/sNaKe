from turtle import Turtle
from time import sleep

class Snake:
    
    direction = 0
    points = 0
    lvl = 1
    length = -1 # 3 elements snake contains 4 elements which one of them is a cover element
    score = 0
    
    def __init__(self, width, height) -> None:
        self.init_board(width, height)
        self.init_score()
        self.alive = True
        self.body = []
        for _ in range(4):
            self.expand_body()
        self.heading = 0
    
    def init_board(self, width, height):
        """ Assign width and height of board for turtles

        Args:
            width (_int_): Width of board, a little bit smaller then width of window
            height (_int_): Height of board, a little bit smaller then height of window
        """
        w = width
        h = height
        self.min_x = -(w // 2)
        self.max_x = w // 2
        self.min_y = -(h // 2)
        self.max_y = h // 2        
    
    def init_score(self):
        """ Initiaties turtle for drawning score and lvl on screen
        """
        self.score_t = Turtle()
        self.score_t.hideturtle()
        self.score_t.up()
        self.score_t.goto(self.min_x, self.min_y)
        self.score_t.write(f"Score: {self.score}, lvl: {self.lvl}")
        
    def show_score(self):
        """ Draws score and lvl on screen with score_t turtle
        """
        self.score_t.clear()
        self.score_t.write(f"Score: {self.score}, lvl: {self.lvl}")
    
    def increase_lvl(self):
        """ Increases lvl of a game, lvl allowed is <1, 5> 

        Returns:
            _int_: Returns number of microsecond for Screen.delay() methon in Screen class
        """
        if self.lvl < 5:
            self.lvl += 1
        self.show_score()
        return self.get_delay()
    
    def decrease_lvl(self):
        """ Decreases lvl of a game, lvl allowed is <1, 5>

        Returns:
            _int_: Returns number of microsecond for Screen.delay() methon in Screen class
        """
        if self.lvl > 1:
            self.lvl -= 1
        self.show_score()
        return self.get_delay()
    
    def get_delay(self):
        """ Getting delay for Screen.delay() method in Screen class

        Returns:
            _int_: Returns number of microsecond for Screen.delay() methon in Screen class
        """
        return 7 - self.lvl
    
    def goto(self, element, x, y):
        """ Moves turtle to defined position by hides it, moves it and showes it again

        Args:
            element (_Turtle_): Turtle object
            x (_int_): x coordinate
            y (_int_): y coordinate
        """
        element.hideturtle()
        element.goto(x, y)
        element.showturtle()
    
    def set_direction(self, direction):
        """ Sets direction for snake preventing from turning back

        Args:
            direction (_int_): same direction as in Turle.setheading() method 0 for east, 90 for north, 180 for west and 270 for south

        Returns:
            _bool_: Returns False when direction cannot be changed or when direction is not 0, 90, 180 or 270
        """
        # direction has to be 0, 90, 180 or 270
        if direction % 90 != 0:
            return False
        
        # preventing from turing back
        if ((self.body[0].heading() + 180) % 360) == direction:
            return False
        
        self.direction = direction
        return True
        
    def move(self):
        """ Moves whole snake one "dot" forward which is 21 pixels
        """
        # set direction for head
        self.body[0].seth(self.direction)
        # remember cover coords
        cover_x, cover_y = self.body[1].pos()
        # move head and tail forward
        # print(f"head id = {self.body[0]} tail id = {self.body[-1]}")
        for i in range(21):
            self.body[-1].fd(1)
            self.body[0].fd(1)
            
            # check collision
            if i == 0:
                if self.check_collision():
                    self.alive = False
                    return
 
        # get head new position
        head_x, head_y = self.body[0].pos()
        
        # pop tail and insert as second element 'at cover position'
        tail = self.body.pop()
        self.goto(tail, cover_x, cover_y)
        self.body.insert(2, tail)
        
        # move cover at head position
        self.goto(self.body[1], head_x, head_y)
        
        # set direction for second element of body
        direction = self.body[0].heading()
        self.body[2].seth(direction)
        
    def expand_body(self):
        """ Expands snake by adding additional segment for body
        """
        t = Turtle("square", visible = False)
        t.up()
        t.speed(0)
        t.color("black")
        if len(self.body) > 2:
            x, y = self.body[-2].pos()
            direction = self.body[-2].heading()
        else:
            x, y = 0, 0
            direction = 0
        t.goto(x, y)
        t.seth(direction)
        t.showturtle()
        self.body.append(t)
        self.length += 1
        
    def get_coords(self):
        """ Returns coordinates of all segments of body

        Returns:
            _List_: List which contains tuplets of coordinates eg. [(1, 1), (1, 2)]
        """
        coords = []
        for segment in self.body:
            coords.append(segment.pos())
        return coords
    
    def get_head_coords(self):
        """Returns coordinates of snake's head

        Returns:
            _tuple_: Tuple with coordinates of snake's head
        """
        return self.body[0].pos()
    
    def eat(self):
        """Method which increase snake's body length, adds points and increases lvl once for 15 segments of a body
        """
        self.score += 1 * self.lvl
        self.expand_body()
        
        # increase lvl every 15 foods
        if self.length % 15 == 0:
            self.increase_lvl()
        self.show_score()
        
    def check_collision(self):
        """Detects collision with a border or with a body of a snake

        Returns:
            _bool_: False for not collided snake and True for detected collision
        """
        head = self.body[0]
        body = self.body[2::]
        
        if self.length > 4:
            for element in body:
                # print(head.distance(element))
                if head.distance(element) < 21:
                    return True
        
        x, y = head.pos()
        if x > self.max_x or x < self.min_x:
            return True
        if y > self.max_y or y < self.min_y:
            return True
        
        return False
        
    def get_head(self):
        """Returns Turle object of the head

        Returns:
            _Turtle_: Turtle of the head
        """
        return self.body[0]
        
        
            
        
        
    