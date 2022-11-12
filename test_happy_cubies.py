import unittest

from happy_cubies import Solution

class TestHappyCubies(unittest.TestCase):
    # Purple Cube
    test_cube = {0: [[0, 0, 1, 0, 1], [1, 1, 0, 1, 0], [0, 0, 0, 1, 1], [1, 1, 0, 1, 0]],
                 1: [[0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]],
                 2: [[0, 0, 1, 1, 1], [1, 0, 1, 0, 0], [0, 0, 1, 1, 1], [1, 0, 1, 1, 0]],
                 3: [[0, 0, 1, 0, 1], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 1, 0]],
                 4: [[0, 0, 0, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0]],
                 5: [[0, 1, 0, 0, 0], [0, 1, 0, 1, 1], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0]]}

    def test_get_cube_line_no_turnover(self):
        '''
        tests the cube line getting function without turnover

        :return:
        '''

        # tile 0, no turnover, edge 0, all orientations
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=0, edge_id=0,
                              expected_line=[0, 0, 1, 0, 1])
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=0, edge_id=0,
                              expected_line=[1, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=0, edge_id=0,
                              expected_line=[0, 0, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=3, turnover_id=0, edge_id=0,
                              expected_line=[1, 1, 0, 1, 0])
        # tile 4, no turnover, edge 0, all orientations
        self.assert_cube_line(tile_id=4, orientation_id=0, turnover_id=0, edge_id=0,
                              expected_line=[0, 0, 0, 1, 1])
        self.assert_cube_line(tile_id=4, orientation_id=1, turnover_id=0, edge_id=0,
                              expected_line=[1, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=4, orientation_id=2, turnover_id=0, edge_id=0,
                              expected_line=[1, 0, 1, 0, 0])
        self.assert_cube_line(tile_id=4, orientation_id=3, turnover_id=0, edge_id=0,
                              expected_line=[0, 1, 0, 1, 0])
        # tile 0, no turnover, all edges, orientation 0
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=0, edge_id=0,
                              expected_line=[0, 0, 1, 0, 1])
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=0, edge_id=1,
                              expected_line=[1, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=0, edge_id=2,
                              expected_line=[0, 0, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=0, edge_id=3,
                              expected_line=[1, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=0, edge_id=4,
                              expected_line=[0, 0, 1, 0, 1])
        # tile 0, no turnover, all edges, orientation 1
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=0, edge_id=0,
                              expected_line=[1, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=0, edge_id=1,
                              expected_line=[0, 0, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=0, edge_id=2,
                              expected_line=[1, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=0, edge_id=3,
                              expected_line=[0, 0, 1, 0, 1])
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=0, edge_id=4,
                              expected_line=[1, 1, 0, 1, 0])
        # tile 0, no turnover, all edges, orientation 2
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=0, edge_id=0,
                              expected_line=[0, 0, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=0, edge_id=1,
                              expected_line=[1, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=0, edge_id=2,
                              expected_line=[0, 0, 1, 0, 1])
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=0, edge_id=3,
                              expected_line=[1, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=0, edge_id=4,
                              expected_line=[0, 0, 0, 1, 1])
        # tile 1, no turnover, all edges, orientation 1
        self.assert_cube_line(tile_id=1, orientation_id=1, turnover_id=0, edge_id=0,
                              expected_line=[0, 0, 0, 1, 0])
        self.assert_cube_line(tile_id=1, orientation_id=1, turnover_id=0, edge_id=1,
                              expected_line=[0, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=1, orientation_id=1, turnover_id=0, edge_id=2,
                              expected_line=[0, 0, 1, 0, 0])
        self.assert_cube_line(tile_id=1, orientation_id=1, turnover_id=0, edge_id=3,
                              expected_line=[0, 0, 1, 0, 0])
        self.assert_cube_line(tile_id=1, orientation_id=1, turnover_id=0, edge_id=4,
                              expected_line=[0, 0, 0, 1, 0])
        # tile 2, no turnover, all edges, orientation 2
        self.assert_cube_line(tile_id=2, orientation_id=2, turnover_id=0, edge_id=0,
                              expected_line=[0, 0, 1, 1, 1])
        self.assert_cube_line(tile_id=2, orientation_id=2, turnover_id=0, edge_id=1,
                              expected_line=[1, 0, 1, 1, 0])
        self.assert_cube_line(tile_id=2, orientation_id=2, turnover_id=0, edge_id=2,
                              expected_line=[0, 0, 1, 1, 1])
        self.assert_cube_line(tile_id=2, orientation_id=2, turnover_id=0, edge_id=3,
                              expected_line=[1, 0, 1, 0, 0])
        self.assert_cube_line(tile_id=2, orientation_id=2, turnover_id=0, edge_id=4,
                              expected_line=[0, 0, 1, 1, 1])
        # tile 3, no turnover, all edges, orientation 3
        self.assert_cube_line(tile_id=3, orientation_id=3, turnover_id=0, edge_id=0,
                              expected_line=[0, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=3, orientation_id=3, turnover_id=0, edge_id=1,
                              expected_line=[0, 0, 1, 0, 1])
        self.assert_cube_line(tile_id=3, orientation_id=3, turnover_id=0, edge_id=2,
                              expected_line=[1, 1, 0, 0, 0])
        self.assert_cube_line(tile_id=3, orientation_id=3, turnover_id=0, edge_id=3,
                              expected_line=[0, 1, 1, 0, 0])
        self.assert_cube_line(tile_id=3, orientation_id=3, turnover_id=0, edge_id=4,
                              expected_line=[0, 1, 0, 1, 0])

    def test_get_cube_line_turnover(self):
        '''
        tests the cube line getting function with turnover

        :return:
        '''

        # tile 0, no turnover, all edges,  orientation 0
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=1, edge_id=0,
                              expected_line=[1, 0, 1, 0, 0])
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=1, edge_id=1,
                              expected_line=[0, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=1, edge_id=2,
                              expected_line=[1, 1, 0, 0, 0])
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=1, edge_id=3,
                              expected_line=[0, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=0, turnover_id=1, edge_id=4,
                              expected_line=[1, 0, 1, 0, 0])
        # tile 0, no turnover, all edges,  orientation 1
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=1, edge_id=0,
                              expected_line=[0, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=1, edge_id=1,
                              expected_line=[1, 1, 0, 0, 0])
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=1, edge_id=2,
                              expected_line=[0, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=1, edge_id=3,
                              expected_line=[1, 0, 1, 0, 0])
        self.assert_cube_line(tile_id=0, orientation_id=1, turnover_id=1, edge_id=4,
                              expected_line=[0, 1, 0, 1, 1])
        # tile 0, no turnover, all edges,  orientation 2
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=1, edge_id=0,
                              expected_line=[1, 1, 0, 0, 0])
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=1, edge_id=1,
                              expected_line=[0, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=1, edge_id=2,
                              expected_line=[1, 0, 1, 0, 0])
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=1, edge_id=3,
                              expected_line=[0, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=2, turnover_id=1, edge_id=4,
                              expected_line=[1, 1, 0, 0, 0])
        # tile 0, no turnover, all edges,  orientation 3
        self.assert_cube_line(tile_id=0, orientation_id=3, turnover_id=1, edge_id=0,
                              expected_line=[0, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=3, turnover_id=1, edge_id=1,
                              expected_line=[1, 0, 1, 0, 0])
        self.assert_cube_line(tile_id=0, orientation_id=3, turnover_id=1, edge_id=2,
                              expected_line=[0, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=0, orientation_id=3, turnover_id=1, edge_id=3,
                              expected_line=[1, 1, 0, 0, 0])
        self.assert_cube_line(tile_id=0, orientation_id=3, turnover_id=1, edge_id=4,
                              expected_line=[0, 1, 0, 1, 1])

        # tile 4, turnover, all edges,  orientation 0
        self.assert_cube_line(tile_id=4, orientation_id=0, turnover_id=1, edge_id=0,
                              expected_line=[1, 1, 0, 0, 0])
        self.assert_cube_line(tile_id=4, orientation_id=0, turnover_id=1, edge_id=1,
                              expected_line=[0, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=4, orientation_id=0, turnover_id=1, edge_id=2,
                              expected_line=[0, 0, 1, 0, 1])
        self.assert_cube_line(tile_id=4, orientation_id=0, turnover_id=1, edge_id=3,
                              expected_line=[1, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=4, orientation_id=0, turnover_id=1, edge_id=4,
                              expected_line=[1, 1, 0, 0, 0])
        # tile 4, turnover, all edges,  orientation 1
        self.assert_cube_line(tile_id=4, orientation_id=1, turnover_id=1, edge_id=0,
                              expected_line=[0, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=4, orientation_id=1, turnover_id=1, edge_id=1,
                              expected_line=[0, 0, 1, 0, 1])
        self.assert_cube_line(tile_id=4, orientation_id=1, turnover_id=1, edge_id=2,
                              expected_line=[1, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=4, orientation_id=1, turnover_id=1, edge_id=3,
                              expected_line=[1, 1, 0, 0, 0])
        self.assert_cube_line(tile_id=4, orientation_id=1, turnover_id=1, edge_id=4,
                              expected_line=[0, 1, 0, 1, 0])
        # tile 4, no turnover, all edges,  orientation 2
        self.assert_cube_line(tile_id=4, orientation_id=2, turnover_id=1, edge_id=0,
                              expected_line=[0, 0, 1, 0, 1])
        self.assert_cube_line(tile_id=4, orientation_id=2, turnover_id=1, edge_id=1,
                              expected_line=[1, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=4, orientation_id=2, turnover_id=1, edge_id=2,
                              expected_line=[1, 1, 0, 0, 0])
        self.assert_cube_line(tile_id=4, orientation_id=2, turnover_id=1, edge_id=3,
                              expected_line=[0, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=4, orientation_id=2, turnover_id=1, edge_id=4,
                              expected_line=[0, 0, 1, 0, 1])
        # tile 4, no turnover, all edges,  orientation 3
        self.assert_cube_line(tile_id=4, orientation_id=3, turnover_id=1, edge_id=0,
                              expected_line=[1, 1, 0, 1, 1])
        self.assert_cube_line(tile_id=4, orientation_id=3, turnover_id=1, edge_id=1,
                              expected_line=[1, 1, 0, 0, 0])
        self.assert_cube_line(tile_id=4, orientation_id=3, turnover_id=1, edge_id=2,
                              expected_line=[0, 1, 0, 1, 0])
        self.assert_cube_line(tile_id=4, orientation_id=3, turnover_id=1, edge_id=3,
                              expected_line=[0, 0, 1, 0, 1])
        self.assert_cube_line(tile_id=4, orientation_id=3, turnover_id=1, edge_id=4,
                              expected_line=[1, 1, 0, 1, 1])

    # test_cube = {0: [[0, 0, 1, 0, 1], [1, 1, 0, 1, 0], [0, 0, 0, 1, 1], [1, 1, 0, 1, 0]],
    #              1: [[0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]],
    #              2: [[0, 0, 1, 1, 1], [1, 0, 1, 0, 0], [0, 0, 1, 1, 1], [1, 0, 1, 1, 0]],
    #              3: [[0, 0, 1, 0, 1], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 1, 0]],
    #              4: [[0, 0, 0, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0]],
    #              5: [[0, 1, 0, 0, 0], [0, 1, 0, 1, 1], [1, 1, 1, 0, 0], [0, 0, 1, 0, 0]]}

    def assert_cube_line(self, tile_id, orientation_id, turnover_id, edge_id, expected_line):
        sol = Solution(cube=self.test_cube)
        a = sol.get_cube_line(tile_id=tile_id, orientation_id=orientation_id, turnover_id=turnover_id, edge_id=edge_id)
        self.assertEqual(a, expected_line)
t     
