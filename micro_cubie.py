import utime as time
from microbit import *

class Solution:
    cube = {}

    tile_sequence = []
    tile_orient = []
    tile_turnover = []

    def __init__(self, cube):
        '''
        Constructor
        :param cube: cube, the solution is tied to
        '''

        self.cube = cube

    # function to check, whether two edges fit into each other
    # pos_edge_1, pos_edge_2 are two 2-tuples with tile-id and
    # edge-id of the tiles/edges to be compared
    def check_edge_compatibility(self, pos_edge_1, pos_edge_2):
        tile_id_1 = self.tile_sequence[pos_edge_1[0]]
        tile_id_2 = self.tile_sequence[pos_edge_2[0]]
        orient_part_1 = self.tile_orient[pos_edge_1[0]]
        orient_part_2 = self.tile_orient[pos_edge_2[0]]
        turnover_part_1 = self.tile_turnover[pos_edge_1[0]]
        turnover_part_2 = self.tile_turnover[pos_edge_2[0]]
        edge_id_1 = pos_edge_1[1]
        edge_id_2 = pos_edge_2[1]

        edge_1_pattern = self.get_cube_line(tile_id=tile_id_1, edge_id=edge_id_1,
                                            orientation_id=orient_part_1, turnover_id=turnover_part_1)
        edge_2_pattern = self.get_cube_line(tile_id=tile_id_2, edge_id=edge_id_2,
                                            orientation_id=orient_part_2, turnover_id=turnover_part_2)

        retval = True
        for i in range(5):
            if i == 0 or i == 4:
                if edge_1_pattern[i] + edge_2_pattern[4 - i] > 1:
                    retval = False
                    break
            elif edge_1_pattern[i] != 1 - edge_2_pattern[4 - i]:
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
            retval = self.check_edge_compatibility(pos_edge_1=(0, 2), pos_edge_2=(1, 0))
        elif solution_pos_id == 3:
            # check edges between pos 2 and 1
            retval = self.check_edge_compatibility(pos_edge_1=(2, 1), pos_edge_2=(1, 3))
            # check edges between pos 2 and 0
            retval = retval and self.check_edge_compatibility(pos_edge_1=(2, 0), pos_edge_2=(0, 3))
        elif solution_pos_id == 4:
            # check edges between pos 1 and 3
            retval = self.check_edge_compatibility(pos_edge_1=(1, 1), pos_edge_2=(3, 3))
            # check edges between pos 0 and 3
            retval = retval and self.check_edge_compatibility(pos_edge_1=(0, 1), pos_edge_2=(3, 0))
        elif solution_pos_id == 5:
            # check edges between pos 1 and 4
            retval = self.check_edge_compatibility(pos_edge_1=(1, 2), pos_edge_2=(4, 0))
            # check edges between pos 2 and 4
            retval = retval and self.check_edge_compatibility(pos_edge_1=(2, 2), pos_edge_2=(4, 3))
            # check edges between pos 3 and 4
            retval = retval and self.check_edge_compatibility(pos_edge_1=(4, 1), pos_edge_2=(3, 2))
        elif solution_pos_id == 6:
            # check edges between pos 4 and 5
            retval = self.check_edge_compatibility(pos_edge_1=(4, 2), pos_edge_2=(5, 0))
            # check edges between pos 5 and 0
            retval = retval and self.check_edge_compatibility(pos_edge_1=(5, 2), pos_edge_2=(0, 0))
            # check edges between pos 5 and 2
            retval = retval and self.check_edge_compatibility(pos_edge_1=(5, 3), pos_edge_2=(2, 3))
            # check edges between pos 5 and 3
            retval = retval and self.check_edge_compatibility(pos_edge_1=(5, 1), pos_edge_2=(3, 1))
        return retval

    # method to remove the last tile from the solution
    def drop_tile(self):
        solution_pos_id = len(self.tile_sequence)
        if solution_pos_id > 0:
            self.tile_sequence.pop()
            self.tile_orient.pop()
            self.tile_turnover.pop()

    # method to add a new tile to the solution
    def add_tile(self, tile_id, orientation_id, turnover_id):
        if tile_id in self.tile_sequence:
            raise ValueError("cannot add tile which is already contained in solution!")
        self.tile_sequence.append(tile_id)
        self.tile_orient.append(orientation_id)
        self.tile_turnover.append(turnover_id)
        if self.check_last_tile_valid():
            retval = True
        else:
            retval = False
            self.drop_tile()
        return retval

    def is_solved(self):
        return len(self.tile_sequence) == 6

    def get_cube_line(self, tile_id, orientation_id, turnover_id, edge_id):
        '''
        return a cube line for a given cube tile, orientation, turnover and edge

        :param cube:
        :param tile_id:
        :param orientation_id:
        :param turnover_id:
        :param edge_id:
        :return:
        '''
        if not turnover_id:
            return self.cube[tile_id][(orientation_id + edge_id) % 4]
        else:
            line_mapping = {0: 0, 1: 3, 2: 2, 3: 1}
            line = self.cube[tile_id][line_mapping[(edge_id + orientation_id) % 4]]
            line = line[::-1]
            return line

# solve the cube. default the position to be chosen will
# be position id = 1, where a deliberate tile can be chosen
# to start from
def solve_cube(cur_sol: Solution):
    # get candidate tiles for future moves
    cand_tiles = list(set(range(6)).difference(set(cur_sol.tile_sequence)))
    cand_tiles.sort()
    turnovers = list(range(2))
    orientations = list(range(4))
    solved = False
    for cand_tile in cand_tiles:
        for orientation in orientations:
            for turnover in turnovers:
                if cur_sol.add_tile(cand_tile, orientation, turnover):
                    if cur_sol.is_solved():
                        solved = True
                        break
                    else:
                        solve_cube(cur_sol)
                        if cur_sol.is_solved():
                            solved = True
                            break
                    cur_sol.drop_tile()
            if solved:
                break
        if solved:
            break
    return cur_sol


def calc_coord(abs_coord):
    dim = 5
    x = y = 0
    if abs_coord < 5:
        x = abs_coord; y = 0
    elif abs_coord < 9:
        x = 4; y = abs_coord - 4
    elif abs_coord < 13:
        x = 12 - abs_coord; y = 4
    else:
        x = 0; y = 16 - abs_coord
    return (x, y)

def get_image_line(image, line_id):
    line = []
    if line_id == 0:
        for x in range(5):
            if image.get_pixel(x, 0) > 0:
                line.append(1)
            else:
                line.append(0)
    elif line_id == 1:
        for y in range(5):
            if image.get_pixel(4, y) > 0:
                line.append(1)
            else:
                line.append(0)
    elif line_id == 2:
        for x in range(4,-1,-1):
            if image.get_pixel(x, 4) > 0:
                line.append(1)
            else:
                line.append(0)
    elif line_id == 3:
        for y in range(4,-1,-1):
            if image.get_pixel(0, y) > 0:
                line.append(1)
            else:
                line.append(0)
    return line

def build_cube(images):
    cube = {}
    cnt = 0
    for image in images:
        cube[cnt] = [get_image_line(image, 0), get_image_line(image, 1),
                   get_image_line(image, 2), get_image_line(image, 3)]
        cnt = cnt + 1
    return cube

def get_solution_string(cur_sol, i):
    front_back_char = "F" if not cur_sol.tile_turnover[i] else "R"    
    output = "Pos {}: {}{}/L{}, ".format(i, front_back_char, cur_sol.tile_sequence[i] + 1, cur_sol.tile_orient[i])
    return output

display.scroll("* Cube Solver *", delay=80)
max_coord = 15
tile_id = -1
new_tile = True
cursor_timestamp = time.ticks_ms()
cursor_dt = 500
cursor_state = False
block_touch = False
both_blocked = False
images = []

while True:
    # preprare new tile
    if new_tile and tile_id < 5:
        new_tile = False
        tile_id = tile_id + 1
        display.scroll("Input Tile {}".format(tile_id + 1), delay=60)
        # storage for patterns
        images.append(Image())
        display.show(Image('00000:'
                           '09990:'
                           '09990:'
                           '09990:'
                           '00000:'))
        
        abs_coord = 0
        x, y = calc_coord(abs_coord)
    elif new_tile:
        # solve loop: Now start solving
        display.scroll("Solving cube...", wait=False)
        cube = build_cube(images)
        cur_sol = Solution(cube)
        solve_cube(cur_sol)
        display.scroll("Cube solved!")
        break
    else:
        # handle events
        if button_a.is_pressed() and button_b.is_pressed():
            if not both_blocked:
                new_tile = True
                both_blocked = True
        else:
            both_blocked = False
        if button_a.was_pressed():
            # paint old position according image data, then move cursor
            display.set_pixel(x, y, images[-1].get_pixel(x, y))
            abs_coord = abs_coord - 1 if abs_coord > 0 else max_coord
            x, y = calc_coord(abs_coord)
        elif button_b.was_pressed():
            # paint old position according image data, then move cursor
            display.set_pixel(x, y, images[-1].get_pixel(x, y))
            abs_coord = abs_coord + 1 if abs_coord < max_coord else 0
            x, y = calc_coord(abs_coord)
        
        # update cursor
        if time.ticks_diff(time.ticks_ms(), cursor_timestamp) >= cursor_dt:
            cursor_state = not cursor_state            
            display.set_pixel(x, y, min(9, 9 * cursor_state + int(images[-1].get_pixel(x, y) * 0.75)))
            cursor_timestamp = time.ticks_ms()

        if pin_logo.is_touched():
            if not block_touch:
                if images[-1].get_pixel(x, y) == 0:
                    images[-1].set_pixel(x, y, 9)            
                else:
                    images[-1].set_pixel(x, y, 0)
                block_touch = True
        else:
            block_touch = False


output = ""
i = 0
display.scroll(get_solution_string(cur_sol, i), loop=True, wait=False)
while True:
    if button_a.was_pressed():
        i = max(0, i - 1)
        display.scroll(get_solution_string(cur_sol, i), loop=True, wait=False)
    if button_b.was_pressed():
        i = min(5, i + 1)
        display.scroll(get_solution_string(cur_sol, i), loop=True, wait=False)
