from window import Window
from point import Point
from line import Line

class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
    
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if(self.has_left_wall):
            top_x = self.__x1
            top_y = self.__y1
            bottom_x = self.__x1
            bottom_y = self.__y2
            top_point = Point(top_x, top_y)
            bottom_point = Point(bottom_x, bottom_y)
            left_line = Line(top_point, bottom_point)
            self.__win.draw_line(left_line, "black")

        if(self.has_right_wall):
            top_x = self.__x2
            top_y = self.__y1
            bottom_x = self.__x2
            bottom_y = self.__y2
            top_point = Point(top_x, top_y)
            bottom_point = Point(bottom_x, bottom_y)
            right_line = Line(top_point, bottom_point)
            self.__win.draw_line(right_line, "black")

        if(self.has_top_wall):
            left_x = self.__x1
            left_y = self.__y1
            right_x = self.__x2
            right_y = self.__y1
            left_point = Point(left_x, left_y)
            right_point = Point(right_x, right_y)
            top_line = Line(left_point, right_point)
            self.__win.draw_line(top_line, "black")

        if(self.has_bottom_wall):
            left_x = self.__x1
            left_y = self.__y2
            right_x = self.__x2
            right_y = self.__y2
            left_point = Point(left_x, left_y)
            right_point = Point(right_x, right_y)
            bottom_line = Line(left_point, right_point)
            self.__win.draw_line(bottom_line, "black")

    def draw_move(self, to_cell, undo=False):
        line_color = "gray"
        if(undo == False):
            line_color = "red"
        this_cell_cen_x = (self.__x2 + self.__x1) / 2
        this_cell_cen_y = (self.__y2 + self.__y1) / 2

        to_cell_cen_x = (to_cell.__x2 + to_cell.__x1) / 2
        to_cell_cen_y = (to_cell.__y2 + to_cell.__y1) / 2

        this_cell_cen = Point(this_cell_cen_x, this_cell_cen_y)
        to_cell_cen = Point(to_cell_cen_x, to_cell_cen_y)

        center_line = Line(this_cell_cen, to_cell_cen)

        self.__win.draw_line(center_line, line_color)