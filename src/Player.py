import pygame as pg
import pathlib

from pg_atlas import PGAtlas

from Structures.Color import *
from Structures.Rect import *
from Structures.Pos import *
from Structures.Sprite import *
from Structures.MSprite import *
from Structures import Constants
from Structures.Enumerator import *


class Player :

    def __init__( self, init_rect: Rect ) :
        self.rect = init_rect
        self.color = Constants.DARK_ICE

        self.walk_east_sprites = []
        self.walk_west_sprites = []
        self.walk_north_sprites = []
        self.walk_south_sprites = []

        self.walk_east_msprite:MSprite = None
        self.walk_west_msprite:MSprite = None
        self.walk_north_msprite:MSprite = None
        self.walk_south_msprite:MSprite = None

        self.__atlas = None
        self.__load_atlas(
            "/home/yolo/Workstation/Python/pygame/Chaotic-Kung-Fu-Kid/assets/images/Walk.json" )

        self.update_sprites()

    def __load_atlas( self, path: str ) :
        self.__atlas = PGAtlas( path )

        self.walk_east_sprites.append( self.__atlas.create_image( "Walk_EAST_0.png" ) )
        self.walk_east_sprites.append( self.__atlas.create_image( "Walk_EAST_1.png" ) )
        self.walk_east_sprites.append( self.__atlas.create_image( "Walk_EAST_2.png" ) )
        self.walk_east_sprites.append( self.__atlas.create_image( "Walk_EAST_3.png" ) )
        self.walk_east_sprites = [Sprite(surface=i) for i in self.walk_west_sprites]

        self.walk_west_sprites.append( self.__atlas.create_image( "Walk_WEST_0.png" ) )
        self.walk_west_sprites.append( self.__atlas.create_image( "Walk_WEST_1.png" ) )
        self.walk_west_sprites.append( self.__atlas.create_image( "Walk_WEST_2.png" ) )
        self.walk_west_sprites.append( self.__atlas.create_image( "Walk_WEST_3.png" ) )
        self.walk_west_sprites = [Sprite(surface=i) for i in self.walk_west_sprites]

        self.walk_north_sprites.append( self.__atlas.create_image( "Walk_NORTH_0.png" ) )
        self.walk_north_sprites.append( self.__atlas.create_image( "Walk_NORTH_1.png" ) )
        self.walk_north_sprites.append( self.__atlas.create_image( "Walk_NORTH_2.png" ) )
        self.walk_north_sprites.append( self.__atlas.create_image( "Walk_NORTH_3.png" ) )
        self.walk_north_sprites = [Sprite(surface=i) for i in self.walk_north_sprites]


        self.walk_south_sprites.append( self.__atlas.create_image( "Walk_SOUTH_0.png" ) )
        self.walk_south_sprites.append( self.__atlas.create_image( "Walk_SOUTH_1.png" ) )
        self.walk_south_sprites.append( self.__atlas.create_image( "Walk_SOUTH_2.png" ) )
        self.walk_south_sprites.append( self.__atlas.create_image( "Walk_SOUTH_3.png" ) )
        self.walk_south_sprites = [Sprite(surface=i) for i in self.walk_south_sprites]


        self.walk_east_msprite = MSprite( self.walk_east_sprites, 0.4 )
        self.walk_west_msprite = MSprite( self.walk_west_sprites, 0.2 )
        self.walk_north_msprite = MSprite( self.walk_north_sprites, 0.4 )
        self.walk_south_msprite = MSprite( self.walk_south_sprites, 0.4 )


    def update_sprites( self ) :
        for i in [self.walk_east_msprite, self.walk_north_msprite, self.walk_west_msprite,
                self.walk_south_msprite] :
            i.reset_scale(self.rect.get_size())
            i.transform_images()

    def set_size( self, size: Pos ) :
        self.rect.get_size().reset( size.x, size.y )


    def check_events( self ) :
        self.walk_west_msprite.check_events()


    def render( self, surface: pg.surface.Surface ) :
        pg.draw.rect( surface, self.color, self.rect )
        self.walk_west_msprite.render(surface,self.rect.get_pos())
