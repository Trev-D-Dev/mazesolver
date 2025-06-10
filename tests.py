import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows
        )

    def test_maze_create_cells_2(self):
        num_cols = 20
        num_rows = 30
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows
        )

    def test_entrance_and_exit(self):
        num_cols = 5
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._Maze__cells[num_cols-1][num_rows-1].has_bottom_wall,
            False
        )

    def test_cells_visited_reset(self):
        num_cols = 5
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        for c in range(num_cols):
            for r in range(num_rows):
                self.assertEqual(
                    m1._Maze__cells[c][r].visited,
                    False
                )

if __name__ == "__main__":
    unittest.main()