from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 800)

    cell_1 = Cell(win)
    cell_2 = Cell(win)
    cell_3 = Cell(win)
    cell_4 = Cell(win)

    cell_1.draw(20, 20, 40, 40)
    cell_2.draw(40, 20, 60, 40)
    cell_3.draw(60, 20, 80, 40)
    cell_4.draw(80, 20, 100, 40)

    win.wait_for_close()

main()