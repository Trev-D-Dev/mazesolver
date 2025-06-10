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
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        walls = ["left", "right", "top", "bottom"]

        for w in range(len(walls)):
            line_color = "black"
            p_1, p_2 = None, None
            match walls[w]:
                case "left":
                    if(not self.has_left_wall):
                        line_color = "white"
                    
                    p_1 = Point(self.__x1, self.__y1)
                    p_2 = Point(self.__x1, self.__y2)
                case "right":
                    if(not self.has_right_wall):
                        line_color = "white"

                    p_1 = Point(self.__x2, self.__y1)
                    p_2 = Point(self.__x2, self.__y2)
                case "top":
                    if(not self.has_top_wall):
                        line_color = "white"

                    p_1 = Point(self.__x1, self.__y1)
                    p_2 = Point(self.__x2, self.__y1)
                case "bottom":
                    if(not self.has_bottom_wall):
                        line_color = "white"
                    
                    p_1 = Point(self.__x1, self.__y2)
                    p_2 = Point(self.__x2, self.__y2)

            line = Line(p_1, p_2)
            self.__win.draw_line(line, line_color)

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