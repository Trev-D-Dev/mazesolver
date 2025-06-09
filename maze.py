from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__cells = []

        self.__create_cells()

    def __create_cells(self):
        self.__cells = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                self.__draw_cell(c, r)

    def __draw_cell(self, i, j):
        x1 = self.x1 + (self.__cell_size_x * i)
        y1 = self.y1 + (self.__cell_size_y * j)
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        self.__cells[i][j] = Cell(self.__win)

        if self.__win:
            self.__cells[i][j].draw(x1, y1, x2, y2)

        self.__animate()

    def __animate(self):
        if self.__win:
            self.__win.redraw()
            time.sleep(0.05)