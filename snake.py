from turtle import Turtle

STARTING_POSITION = ((0,0), (-20,0), (-40,0))
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]
        self._turning = False

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        if self.segment_list:
            pass
        else:
            new_segment = Turtle("circle")
            new_segment.color("red")
            new_segment.shapesize(1)
            new_segment.penup()
            new_segment.goto(position)
            self.segment_list.append(new_segment)
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(0.8)
        new_segment.penup()
        new_segment.goto(position)
        self.segment_list.append(new_segment)
        print(self.segment_list[-1])

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        for segment_number in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[segment_number - 1].xcor()
            new_y = self.segment_list[segment_number - 1].ycor()
            self.segment_list[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self._turning = False

    def up(self):
        if not self._turning and self.head.heading() != DOWN:
            self.head.setheading(UP)
            self._turning = True

    def down(self):
        if not self._turning and self.head.heading() != UP:
            self.head.setheading(DOWN)
            self._turning = True

    def left(self):
        if not self._turning and self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self._turning = True

    def right(self):
        if not self._turning and self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self._turning = True







