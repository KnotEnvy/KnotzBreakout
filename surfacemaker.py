import pygame as py
from settings import *
from os import walk
class SurfaceMaker:
    def __init__(self):
    #import all graphics
        for index, info in enumerate(walk('graphics/blocks')):
            if index == 0:
                self.assets = {color:{} for color in info[1]}
            else:
                for image_name in info[2]:
                    color_type = list(self.assets.keys())[index - 1]
                    full_path = 'graphics/blocks' + f'/{color_type}/' + image_name
                    surf = py.image.load(full_path).convert_alpha()
                    self.assets[color_type][image_name.split('.')[0]] = surf
    #create one surface with scalable graphics

    def get_surf(self, block_type, size):
        image = py.Surface(size)
        image.set_colorkey((0,0,0))
        sides = self.assets[block_type]

        #4 corners
        image.blit(sides['topleft'], (0,0))
        image.blit(sides['topright'], (size[0] - sides['topright'].get_width(),0))
        image.blit(sides['bottomleft'], (0, size[1] - sides['bottomleft'].get_height()))
        image.blit(sides['bottomright'], (size[0] - sides['bottomright'].get_width(), size[1] - sides['bottomright'].get_height()))
        
        #top side
        top_width = size[0] - (sides['topleft'].get_width() + sides['topright'].get_width())
        scaled_top_surf = py.transform.scale(sides['top'], (top_width,sides['top'].get_height()))
        image.blit(scaled_top_surf, (sides['topleft'].get_width(), 0))

        #left side
        left_height = size[1] - (sides['topleft'].get_height() + sides['bottomleft'].get_height())
        scaled_left_surf = py.transform.scale(sides['left'],(sides['left'].get_width(),left_height))
        image.blit(scaled_left_surf, (0, sides['topleft'].get_height()))
        
        #right side
        right_height = size[1] - (sides['topright'].get_height() + sides['bottomright'].get_height())
        scaled_right_surf = py.transform.scale(sides['right'],(sides['right'].get_width(), right_height))
        image.blit(scaled_right_surf, (size[0] - sides['right'].get_width(), sides['topright'].get_height()))
        
        #bottom side
        bottom_width = size[0] - (sides['bottomleft'].get_width() + sides['bottomright'].get_width())
        scaled_bottom_surf = py.transform.scale(sides['bottom'], (top_width,sides['bottom'].get_height()))
        image.blit(scaled_bottom_surf, (sides['topleft'].get_width(), size[1]- sides['bottom'].get_height()))
        
        # center color
        center_height = size[1] - (sides['top'].get_height() + sides['bottom'].get_height())
        center_width = size[0] - (sides['right'].get_width() + sides['left'].get_width())
        scaled_center = py.transform.scale(sides['center'], (center_width, center_height))
        image.blit(scaled_center, sides['topleft'].get_size())
    
    
    #return image to blocks or player
        return image