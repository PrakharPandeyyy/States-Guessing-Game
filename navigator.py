from turtle import Turtle


class Navigator(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def new_turtle(self, city, x, y):
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(x, y)
        self.write(city, font=("Courier", 8, "normal"))


