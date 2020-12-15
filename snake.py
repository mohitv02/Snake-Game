from turtle import Turtle

INIT_DIST = [0, -20, -40, -60]
CONT_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for a in range(3):
            position = [INIT_DIST[a], 0]
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.segment.append(turtle)

    def extent(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x_cor = self.segment[seg - 1].xcor()
            y_cor = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x=x_cor, y=y_cor)
        self.head.forward(CONT_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
