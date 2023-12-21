#!/usr/bin/env python3

# Created by: Redd Forfieda
# Created on:december 19 2023
# This program is the "space Alien" program on the PyBadge

import ugame
import stage


def game_scene():
    #this function is the main game game_scene
 
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    background = stage.Grid(image_bank_background, 10, 8)

    #set the background to image 0 in the image bank
    #   and the size(10x8 tiles of size 16x16)
    # a sprite that will be updated every frame 
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    game = stage.Stage(ugame.display, 60)
   
    # set the layers of all spirites, items show up in order
    game.layers = [ship] + [background]
    # renders all sprites
    # mostlikesly you will render the background once per game scene
    game.render_block()
    
    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        # redraw sprites
        game.render_sprites([ship])
        game.tick()
        

if __name__  == "__main__":
    game_scene()  