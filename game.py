import pygame as py
import sys, time
from settings import *
from sprites import Player, Ball, Block, Upgrade, Projectile
from surfacemaker import SurfaceMaker
from random import choice, randint

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
        self.block_sprites = py.sprite.Group()
        self.upgrade_sprites = py.sprite.Group()
        self.projectile_sprites = py.sprite.Group()
 
        #setup for sprites
        self.surfacemaker = SurfaceMaker()
        self.player = Player(self.all_sprites, self.surfacemaker)
        self.stage_setup()
        self.ball = Ball(self.all_sprites, self.player, self.block_sprites)
        
        #hearts
        self.heart_surf = py.image.load('graphics/other/heart.png').convert_alpha()
        #projectile
        self.projectile_surf = py.image.load('graphics/other/projectile.png').convert_alpha()
        self.can_shoot = True
        self.shoot_time = 0

        #crt
        self.crt = CRT()
        #sounds
        self.laser_sound = py.mixer.Sound('sounds/laser.wav')
        self.laser_sound.set_volume(0.1)

        self.powerup_sound = py.mixer.Sound('sounds/powerup.wav')
        self.powerup_sound.set_volume(0.1)

        self.laserhit_sound = py.mixer.Sound('sounds/laser_hit.wav')
        self.laserhit_sound.set_volume(0.02)

        self.music = py.mixer.Sound('sounds/music.wav')
        self.music.set_volume(0.1)
        self.music.play(loops = -1)



    def create_upgrade(self, pos ):
        upgrade_type = choice(UPGRADES)
        Upgrade(pos, upgrade_type, [self.all_sprites, self.upgrade_sprites])

    def create_bg(self):
        bg_original = py.image.load('graphics/other/bg2.png').convert_alpha()
        scale_factor = WINDOW_HEIGHT / bg_original.get_height()
        scaled_width = bg_original.get_width() * scale_factor
        scaled_height = bg_original.get_height() * scale_factor
        scaled_bg = py.transform.scale(bg_original, (scaled_width, scaled_height))
        return scaled_bg

    def stage_setup(self):
        #cycle through rows and columns of block map
        for row_index, row in enumerate(BLOCK_MAP):
            for col_index, col in enumerate(row):
                if col != ' ':
                    #find postion of all blocks
                    x = col_index * (BLOCK_WIDTH + GAP_SIZE) + GAP_SIZE // 2
                    y = TOP_OFFSET + row_index * (BLOCK_HEIGHT + GAP_SIZE) + GAP_SIZE // 2
                    Block(col, (x,y), [self.all_sprites, self.block_sprites], self.surfacemaker, self.create_upgrade)

    def display_hearts(self):
        for i in range(self.player.hearts):
            x = 2 + i * (self.heart_surf.get_width() + 2)
            self.display_surface.blit(self.heart_surf, (x,4))

    def upgrade_collision(self):
        overlap_sprites =py.sprite.spritecollide(self.player, self.upgrade_sprites, True)
        for sprite in overlap_sprites:
            self.player.upgrade(sprite.upgrade_type)
            self.powerup_sound.play()

    def create_projectile(self):
        self.laser_sound.play()
        for projectile in self.player.laser_rects:
            Projectile(projectile.midtop - py.math.Vector2(0, 30), 
                       self.projectile_surf, [self.all_sprites, self.projectile_sprites])

    def laser_timer(self):
        if py.time.get_ticks() - self.shoot_time >= 500:
                   self.can_shoot = True

    def projectile_collision(self):
        for projectile in self.projectile_sprites:
            overlap_sprites = py.sprite.spritecollide(projectile, self.block_sprites, False)
            if overlap_sprites:
                for sprite in overlap_sprites:
                    sprite.get_damage(1)
                projectile.kill()
                self.laserhit_sound.play()

    def run(self):
        last_time = time.time()
        while True:
            #delta time
            dt = time.time() - last_time
            last_time  = time.time()

            #event loop
            for event in py.event.get():
                if event.type == py.QUIT or self.player.hearts <= 0: #remember to change ENDGAME
                    py.quit()
                    sys.exit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_SPACE:
                        self.ball.active = True
                        if self.can_shoot:
                            self.create_projectile()
                            self.can_shoot = False
                            self.shoot_time = py.time.get_ticks()

            #draw background
            self.display_surface.blit(self.bg, (0,0))
            #update the game
            self.all_sprites.update(dt)
            self.upgrade_collision()
            self.laser_timer()
            self.projectile_collision()
            #draw frame
            self.all_sprites.draw(self.display_surface)
            self.display_hearts()

            #crt styling
            self.crt.draw()

            #update window
            py.display.update()

class CRT:
    def __init__(self):
        vignette = py.image.load('graphics/other/tv.png').convert_alpha()
        self.scaled_vignette = py.transform.scale(vignette,(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display_surface = py.display.get_surface()
        self.create_crt_lines()

    def create_crt_lines(self):
        line_height = 4
        line_amount = WINDOW_HEIGHT // line_height
        for line in range(line_amount):
            y = line * line_height
            py.draw.line(self.scaled_vignette, 'black', (0, y), (WINDOW_WIDTH,y), 1)

    def draw(self):
        self.scaled_vignette.set_alpha(randint(60, 75))
        self.display_surface.blit(self.scaled_vignette,(0,0))

if __name__ == '__main__':
    game = Game()
    game.run()