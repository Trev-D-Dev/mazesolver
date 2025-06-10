from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    seed = 10

    # line for testing with seed
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)

    # line for testing seedless
    # maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    maze.solve()

    win.wait_for_close()

main()