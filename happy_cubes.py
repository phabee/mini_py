# Imports go at the top
# from microbit import *
import copy

# Strategic comments:
# we first try to solve the cube without flipping the
# parts. if necessary, this will be an additional flavour
# of variation and increase the number of possible moves
# in every step.

# definition orange happy cube (hole upper right)
# define square-parts-edge patterns from left to right and
# top to bottom for all 6 cube square-parts
cube = {0: [[1,0,1,0,1],[1,1,0,1,1],[1,0,0,1,0],[0,1,0,1,1]],
        1: [[0,0,0,1,0],[0,1,0,1,0],[0,0,1,0,0],[0,0,1,0,0]],
        2: [[0,0,1,1,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,1,0,0]],
        3: [[0,1,0,1,0],[0,1,1,0,0],[0,0,1,0,1],[1,1,0,1,0]],
        4: [[1,1,0,0,0],[0,1,0,1,0],[0,1,0,1,1],[1,0,1,0,1]],
        5: [[0,1,0,1,1],[1,0,1,0,1],[1,1,0,1,0],[0,0,1,0,0]]}

class Solution:
    tile_sequence = []
    tile_orient = []
    
    # function to check, whether two edges fit into each other
    # pos_edge_1, pos_edge_2 are two 2-tuples with tile-id and 
    # edge-id of the tiles/edges to be compared
    # alt_dir = True per default, indicating, that the sequence
    # of edge-patterns have to be inverted on one component,
    # before comparison takes place
    def check_edge_compatibility(self, pos_edge_1, pos_edge_2,
                     alt_dir=True):
        part_id_1 = self.tile_sequence[pos_edge_1[0]]
        part_id_2 = self.tile_sequence[pos_edge_2[0]]
        orient_part_1 = self.tile_orient[pos_edge_1[0]]
        orient_part_2 = self.tile_orient[pos_edge_2[0]]
        edge_id_1 = pos_edge_1[1]
        edge_id_2 = pos_edge_2[1]
        
        edge_1_pattern = cube[part_id_1][(edge_id_1 + orient_part_1)%4]
        edge_2_pattern = cube[part_id_2][(edge_id_2 + orient_part_2)%4]
        
        retval = True
        for i in range(5):
            if alt_dir:
                if i == 0 or i == 4:
                    if edge_1_pattern[i] + edge_2_pattern[4-i] > 1:
                        retval = False
                        break
                elif edge_1_pattern[i] != 1 - edge_2_pattern[4-i]:
                    retval = False
                    break
            else:
                if i == 0 or i == 4:
                    if edge_1_pattern[i] + edge_2_pattern[i] > 1:
                        retval = False
                        break
                elif edge_1_pattern[i] != 1 - edge_2_pattern[i]:
                    retval = False
                    break
        return retval
        
    # function to check, whether a given tile can be inserted as the
    # next tile in the given orientation and matches all existing
    # tiles pos_ids
    #   0
    # 2 1 3
    #   4
    #   5
    def check_last_tile_valid(self):
        solution_pos_id = len(self.tile_sequence)
        retval = False
        if solution_pos_id <= 1:
            retval = True
        elif solution_pos_id == 2:
            # only check edges between pos 0 and 1
            retval = self.check_edge_compatibility(pos_edge_1 = (0,2), pos_edge_2 = (1,0))
        elif solution_pos_id == 3:
            # check edges between pos 2 and 1
            retval = self.check_edge_compatibility(pos_edge_1 = (2,1), pos_edge_2 = (1,3))
            # check edges between pos 2 and 0
            retval = retval and self.check_edge_compatibility(pos_edge_1 = (2,0), pos_edge_2 = (0,3))
        elif solution_pos_id == 4:
            # check edges between pos 1 and 3
            retval = self.check_edge_compatibility(pos_edge_1 = (1,2), pos_edge_2 = (3,3))
            # check edges between pos 0 and 3
            retval = retval and self.check_edge_compatibility(pos_edge_1 = (0,1), pos_edge_2 = (3,0))
        elif solution_pos_id == 5:
            # check edges between pos 1 and 4
            retval = self.check_edge_compatibility(pos_edge_1 = (1,2), pos_edge_2 = (4,0))
            # check edges between pos 2 and 4
            retval = retval and self.check_edge_compatibility(pos_edge_1 = (2,2), pos_edge_2 = (4,3))
            # check edges between pos 3 and 4
            retval = retval and self.check_edge_compatibility(pos_edge_1 = (3,2), pos_edge_2 = (4,1))
        elif solution_pos_id == 6:
            # check edges between pos 4 and 5
            retval = self.check_edge_compatibility(pos_edge_1 = (4,2), pos_edge_2 = (5,0))
            # check edges between pos 5 and 0
            retval = retval and self.check_edge_compatibility(pos_edge_1 = (5,2), pos_edge_2 = (0,0))
            # check edges between pos 5 and 2
            retval = retval and self.check_edge_compatibility(pos_edge_1 = (5,3), pos_edge_2 = (2,3), alt_dir=False)
            # check edges between pos 5 and 3
            retval = retval and self.check_edge_compatibility(pos_edge_1 = (5,1), pos_edge_2 = (3,1), alt_dir=False)
        return retval

    # method to remove the last tile from the solution
    def drop_tile(self):
        solution_pos_id = len(self.tile_sequence)
        if solution_pos_id > 0:
            self.tile_sequence.pop()
            self.tile_orient.pop()
        
    # method to add a new tile to the solution
    def add_tile(self, tile_id, orientation_id):
        if tile_id in self.tile_sequence:
            raise ValueError("cannot add tile which is already contained in solution!")
        self.tile_sequence.append(tile_id)
        self.tile_orient.append(orientation_id)
        if self.check_last_tile_valid():
            retval = True
        else:
            retval = False
            self.drop_tile()
        return retval

    def is_solved(self):
        return len(self.tile_sequence) == 6

# solve the cube. default the position to be chosen will
# be position id = 1, where a deliberate tile can be chosen
# to start from
def solve_cube(cube, cur_sol:Solution):
    # get candidate tiles for future moves
    print(cur_sol.tile_sequence)
    cand_tiles = list(set(range(6)).difference(set(cur_sol.tile_sequence)))
    cand_tiles.sort()
    orientations = list(range(4))
    solved = False
    for cand_tile in cand_tiles:
        for orientation in orientations:
            if cur_sol.add_tile(cand_tile, orientation):
                if cur_sol.is_solved():
                    solved = True
                    break
                else:
                    solve_cube(cube, cur_sol)
                    if cur_sol.is_solved():
                        solved = True
                        break
                cur_sol.drop_tile()
        if solved:
            break
    return cur_sol

cur_sol = Solution()
result = solve_cube(cube, cur_sol)
print(result.tile_sequence)
print(result.tile_orient)
