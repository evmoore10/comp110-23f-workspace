"""Creating a Track and Field!"""

__author__ = "730670009"

from turtle import Turtle, colormode, done 


def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)
    speed: Turtle = Turtle()
    speed.speed(20)
    background(speed)
    i: int = 0
    j: float = 1.0
    while i < 6:
        draw_track(speed, j)
        j -= .1
        i += 1
    discus(speed)
    shotput(speed)
    done()


def draw_track(speed: Turtle, scale_factor: float) -> None:
    """Draws a track with scale factor."""
    speed.fillcolor("sandybrown")
    speed.penup()
    speed.goto(-250 * scale_factor, 200 * scale_factor)
    """Used a scale factor here to complete the track as apart of trying something fun."""
    change: float = 100 * (1.0 - scale_factor)
    speed.pendown()
    speed.begin_fill()
    speed.pencolor("white")
    speed.forward(500 * scale_factor)
    speed.circle(-120 * scale_factor + change, 180)
    speed.forward(500 * scale_factor)
    speed.circle(-120 * scale_factor + change, 180)
    speed.end_fill()


def background(speed: Turtle) -> None:
    """Fills background in."""
    speed.fillcolor("green")
    speed.penup()
    speed.goto(-500, -500)
    speed.pendown()
    speed.begin_fill()
    for each in range(4):
        speed.forward(1000)
        speed.left(90)
    speed.end_fill()
    

def discus(speed: Turtle) -> None:
    """Creates discus pit."""

    def net(speed: Turtle) -> None:
        """Creates a net around the pit."""
        speed.penup()
        speed.width(3)
        speed.pencolor("black")
        speed.goto(200, -280)
        speed.pendown()
        speed.circle(60, 200)
        speed.pencolor("white")

    def foul_lines(speed: Turtle) -> None:
        """Creates the sector lines."""
        speed.penup()
        speed.width(1.5)
        speed.goto(190, -248)
        speed.pendown()
        speed.left(10)
        speed.forward(400)
        speed.penup()
        speed.goto(178, -200)
        speed.right(35)
        speed.pendown()
        speed.forward(400)
    
    speed.fillcolor("grey")
    speed.penup()
    speed.goto(200, -250)
    speed.begin_fill()
    speed.pendown()
    speed.circle(30)
    speed.end_fill()
    net(speed)
    foul_lines(speed)


def shotput(speed: Turtle) -> None:
    """Creates shotput pit."""
    
    def foul_lines(speed: Turtle) -> None:
        """Draws the sector lines."""
        speed.penup()
        speed.width(1.5)
        speed.goto(-157, 300)
        speed.pendown()
        speed.right(15)
        speed.forward(200)
        speed.penup()
        speed.goto(-157, 340)
        speed.pendown()
        speed.left(30)
        speed.forward(200)
    
    speed.fillcolor("grey")
    speed.penup()
    speed.width(1)
    speed.setheading(0)
    speed.goto(-180, 290)
    speed.begin_fill()
    speed.pendown()
    speed.circle(30)
    speed.end_fill()
    foul_lines(speed)


if __name__ == "__main__":
    main()