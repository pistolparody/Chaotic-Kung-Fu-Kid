import pygame as pg

from Player import Player

from Structures.Color import *
from Structures.Rect import *
from Structures.Pos import *
from Structures.Sprite import *
from Structures.MSprite import *
from Structures import Constants
from Structures.Enumerator import *


class Game:
    def __init__( self , surface_size:Pos):
        self.surface_size = surface_size
        self.background_color = Constants.DEEP_DARK_RED
        self.should_render_debug = False

        self.player = Player(
            Rect.fromPos(self.surface_size.get_transformed_pos(mult=0.5),
                         self.surface_size.get_transformed_pos(mult=0.1)))




    def get_events( self, event_list:list = None):
        if event_list is None: event_list = pg.event.get()

        for i in event_list:
            pass


    def check_events( self ):
        pass

    def render_debug( self , surface:pg.surface.Surface ):
        pg.draw.line( surface, [180, 180, 180], [self.surface_size.x / 2, 0],
            [self.surface_size.x / 2, self.surface_size.y] )

        pg.draw.line( surface, [180, 180, 180], [0, self.surface_size.y / 2],
            [self.surface_size.x, self.surface_size.y / 2] )

    def render( self , surface:pg.surface.Surface):
        surface.fill(self.background_color)

        self.player.render(surface)


        if self.should_render_debug: self.render_debug(surface)


