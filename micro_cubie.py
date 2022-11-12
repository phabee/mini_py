import utime as time
from microbit import *


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
    print("x,y:", x,y)
    return (x, y)

#display.scroll("* Cube Solver *", delay=40)
max_coord = 15
tile_id = -1
new_tile = True
cube = {0: [00000]}
cursor_timestamp = time.ticks_ms()
cursor_dt = 500
cursor_state = False

images = []

while True:
    # preprare new tile
    if new_tile:
        # display.scroll("Input Tile {}".format(tile_id + 1), delay=40)
        new_tile = False
        tile_id = tile_id + 1
        # storage for patterns
        images.append(Image())
        display.show(Image('00000:'
                           '09990:'
                           '09990:'
                           '09990:'
                           '00000:'))
        
        abs_coord = 0
        x, y = calc_coord(abs_coord)
    else:
        # handle events
        if button_a.was_pressed():
            # paint old position according image data, then move cursor
            display.set_pixel(x, y, images[-1].get_pixel(x, y))
            abs_coord = abs_coord - 1 if abs_coord > 0 else max_coord
            x, y = calc_coord(abs_coord)
        if button_b.was_pressed():
            # paint old position according image data, then move cursor
            display.set_pixel(x, y, images[-1].get_pixel(x, y))
            abs_coord = abs_coord + 1 if abs_coord < max_coord else 0
            x, y = calc_coord(abs_coord)
        if pin_logo.is_touched():
            if images[-1].get_pixel(x, y) == 0:
                images[-1].set_pixel(x, y, 9)            
            else:
                images[-1].set_pixel(x, y, 0)            
        # update cursor
        if time.ticks_diff(time.ticks_ms(), cursor_timestamp) >= cursor_dt:
            cursor_state = not cursor_state            
            display.set_pixel(x, y, min(9, 9 * cursor_state + int(images[-1].get_pixel(x, y) * 0.75)))
            cursor_timestamp = time.ticks_ms()
        
            
    
