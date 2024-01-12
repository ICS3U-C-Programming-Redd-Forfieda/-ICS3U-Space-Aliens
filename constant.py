#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: October 2019
# This constants file is for Space Alien game

# CircuitPython screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
FPS = 60
SPRITE_MOVEMENT_SPEED = 1


# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just_pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"

}
# new pallet for red filled text
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'

              b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
