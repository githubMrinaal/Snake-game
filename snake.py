from turtle import Turtle
import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ["green","blue","white","red","orange","yellow"]

class Snake:

    
    def __init__(self):
        self.segments = []
        starting_position = [(0,0),(-20,0),(-40,0)]

        for position in starting_position:
            self.add_segment(position)
            

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def extend(self):
        #add a new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(random.choice(COLORS))
        new_segment.penup() 
        new_segment.goto(position)
        self.segments.append(new_segment)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
    
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)