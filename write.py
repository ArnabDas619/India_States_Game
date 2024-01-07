from turtle import Turtle


class Write:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.pencolor("black")
        self.turtle.penup()

    def screen_write(self, text, x, y):
        self.turtle.goto(x, y)
        self.turtle.write(arg=text, align="center", font=('Arial', 8, 'normal'))
