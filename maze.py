from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__cells = []

        if(seed):
            random.seed(seed)

        self.__create_cells()

        self.__break_walls_r(0, 0)

        self.__reset_cells_visited()

    def __create_cells(self):
        self.__cells = [[Cell(self.__win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]

        self.__break_entrance_and_exit()

        for c in range(self.num_cols):
            for r in range(self.num_rows):
                self.__draw_cell(c, r)

    def __draw_cell(self, i, j):
        x1 = self.x1 + (self.__cell_size_x * i)
        y1 = self.y1 + (self.__cell_size_y * j)
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        if self.__win:
            self.__cells[i][j].draw(x1, y1, x2, y2)
            self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        # top left cell
        self.__cells[0][0].has_top_wall = False
        #self.__draw_cell(0, 0)

        c = self.num_cols - 1
        r = self.num_rows - 1

        # bottom right cell
        self.__cells[-1][-1].has_bottom_wall = False
        #self.__draw_cell(c, r)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self.__cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self.__cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self.__draw_cell(i, j)
                return
            
            # randomly chooses the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out the walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self.__break_walls_r(next_index[0], next_index[1])

    def __reset_cells_visited(self):
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                self.__cells[c][r].visited = False

    def solve(self):
        result = self.__solve_r(0, 0)
        return result
    
    def __solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True

        c_cell = self.__cells[i][j]

        # checks if current cell is end cell
        if((i == self.num_cols - 1) and (j == self.num_rows - 1)):
            return 
        
        # check cells in each direction
        # left
        if i > 0 and not self.__cells[i - 1][j].visited:
            if (not self.__cells[i][j].has_left_wall) and not self.__cells[i - 1][j].has_right_wall:
                l_cell = self.__cells[i - 1][j]
                c_cell.draw_move(l_cell)
                result = self.__solve_r(i - 1, j)
                if(result):
                    return True
                c_cell.draw_move(l_cell, True)

        # right
        if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
            if (not self.__cells[i][j].has_right_wall) and not self.__cells[i + 1][j].has_left_wall:
                r_cell = self.__cells[i + 1][j]
                c_cell.draw_move(r_cell)
                result = self.__solve_r(i + 1, j)
                if(result):
                    return True
                c_cell.draw_move(r_cell, True)

        # up
        if j > 0 and not self.__cells[i][j - 1].visited:
            if (not self.__cells[i][j].has_top_wall) and not self.__cells[i][j - 1].has_bottom_wall:
                u_cell = self.__cells[i][j - 1]
                c_cell.draw_move(u_cell)
                result = self.__solve_r(i, j - 1)
                if(result):
                    return True
                c_cell.draw_move(u_cell, True)

        # down
        if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
            if (not self.__cells[i][j].has_bottom_wall) and not self.__cells[i][j + 1].has_top_wall:
                d_cell = self.__cells[i][j + 1]
                c_cell.draw_move(d_cell)
                result = self.__solve_r(i, j + 1)
                if(result):
                    return True
                c_cell.draw_move(d_cell, True)

        # if no directions worked out
        return False