from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 800)

    point_a = Point(5, 10)
    point_b = Point(30, 40)
    line_a = Line(point_a, point_b)
    win.draw_line(line_a, "red")

    win.wait_for_close()

main()