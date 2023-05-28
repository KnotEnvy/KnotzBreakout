import pygame as py
import sys, time
from settings import *
from sprites import Player

class Game:
    def __init__(self):

        #generl setup
        py.init()
        self.display_surface = py.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        py.display.set_caption('KnotzBreakOut')

        #background
        self.bg = self.create_bg()

        #sprite group setup
        self.all_sprites = py.sprite.Group()

        #setup for sprites
        self.player = Player(self.all_sprites)

    def create_bg(self):
        bg_original = py.image.load('graphics/other/bg.png').convert_alpha()
        scale_factor = WINDOW_HEIGHT / bg_original.get_height()
        scaled_width = bg_original.get_width() * scale_factor
        scaled_height = bg_original.get_height() * scale_factor
        scaled_bg = py.transform.scale(bg_original, (scaled_width, scaled_height))
        return scaled_bg


    def run(self):
        last_time = time.time()
        while True:
            

            #delta time
            dt = time.time() - last_time
            last_time  = time.time()

            #event loop
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

            #update the game
            self.all_sprites.update(dt)
            
            #draw frame
            self.display_surface.blit(self.bg, (0,0))
            self.all_sprites.draw(self.display_surface)

            #update window
            py.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()