# create snake, extend snake, snake moving functionality using keys.
from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for position in POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.shapesize()  # change size of turtle,default 20px. turtle.shapesize(stretch_wid,stretch_len,outline)
        self.all_segments.append(new_segment)

    def snake_reset(self):
        for seg in self.all_segments:  # so that the old snake disappear from the screen, send dead snake at (1000,1000)
            seg.goto(1000, 1000)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]

    def extend(self):
        # turtle method position() returns a tuple containing (x, y) coordinates of the turtle's current position
        self.add_segment(self.all_segments[-1].position())  # get tail position (x,y)

    def move(self):
        for segment in range(len(self.all_segments) - 1, 0, -1):  # ex.[(0, 0),(-20, 0),(-40, 0)], range(start,end,step)
            new_x = self.all_segments[segment - 1].xcor()   # e.g. new_x = -20
            new_y = self.all_segments[segment - 1].ycor()   # e.g. new_y = 0
            self.all_segments[segment].goto(new_x, new_y)   # e.g. move (-40, 0) to (-20, 0)
        self.all_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # heading() returns the current heading as an angle in degrees
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
