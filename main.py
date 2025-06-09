from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 800)

    maze = Maze(25, 25, 30, 20, 25, 25, win)

    win.wait_for_close()

main()