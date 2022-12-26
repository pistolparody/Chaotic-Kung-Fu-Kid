import pygame as pg
import pathlib

from pg_atlas import PGAtlas

from Structures.Color import *
from Structures.Rect import *
from Structures.Pos import *
from Structures.Sprite import *
from Structures.MSprite import *
from Structures import Constants as c
from Structures.Enumerator import *
from PlayerAssets import PlayerAssets

class Player(PlayerAssets) :

    def __init__( self, init_rect: Rect ) :
        super().__init__()

        self.rect = init_rect
        self.color = c.DARK_ICE

        self.direction = c.WEST
        self.state = c.IDLE
        self.move_speed_scale = 0.03

        self.is_moving = False
        self.should_render_debug = False

        self.__atlas = None

        self.update_sprites()



    def update_sprites( self ) :
        x_scale = self.rect.height / self.walk_east_sprites[0].get_raw_size().y

        for i in [self.walk_east_msprite, self.walk_north_msprite, self.walk_west_msprite,
                     self.walk_south_msprite] + [self.idle_east_msprite, self.idle_north_msprite,
                     self.idle_west_msprite, self.idle_south_msprite] :
            i.reset_scale(Pos(x_scale, x_scale))
            i.transform_images()

    def get_center( self ) :
        return self.rect.get_pos().join(self.rect.get_size().get_transformed_pos(mult=0.5))


    def set_size( self, size: Pos ) :
        self.rect.get_size().reset(size.x, size.y)


    def move( self ) :
        if self.direction == c.NORTH :
            self.rect.y -= self.rect.height * self.move_speed_scale
        elif self.direction == c.SOUTH :
            self.rect.y += self.rect.height * self.move_speed_scale
        elif self.direction == c.EAST :
            self.rect.x += self.rect.width * self.move_speed_scale
        elif self.direction == c.WEST :
            self.rect.x -= self.rect.width * self.move_speed_scale

        if self.rect.x < self.rect.width :
            pass
        if self.rect.y < self.rect.height :
            pass


    def check_events( self ) :
        if self.is_moving :
            self.state = c.WALK
            self.move()
        else :
            self.state = c.IDLE

        target_msprite = self.atlas_table[self.state][self.direction]

        target_msprite.check_events()


    def render_debug( self, surface: pg.surface.Surface ) :
        pg.draw.rect(surface, self.color, self.rect)


    def render( self, surface: pg.surface.Surface ) :
        if self.should_render_debug : self.render_debug(surface)

        target_msprite = self.atlas_table[self.state][self.direction]

        target_msprite.render(surface, self.get_center())




