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


class Player :

    def __init__( self, init_rect: Rect ) :
        self.rect = init_rect
        self.color = c.DARK_ICE

        self.direction = c.WEST
        self.state = c.IDLE
        self.move_speed_scale = 0.1

        self.is_moving = False

        self.walk_east_sprites:list[Sprite] = []
        self.walk_west_sprites:list[Sprite] = []
        self.walk_north_sprites:list[Sprite] = []
        self.walk_south_sprites:list[Sprite] = []

        self.walk_east_msprite:MSprite = None
        self.walk_west_msprite:MSprite = None
        self.walk_north_msprite:MSprite = None
        self.walk_south_msprite:MSprite = None

        self.idle_east_sprites: list[Sprite] = []
        self.idle_west_sprites: list[Sprite] = []
        self.idle_north_sprites: list[Sprite] = []
        self.idle_south_sprites: list[Sprite] = []

        self.idle_east_msprite: MSprite = None
        self.idle_west_msprite: MSprite = None
        self.idle_north_msprite: MSprite = None
        self.idle_south_msprite: MSprite = None

        self.__atlas = None
        self.__load_atlas(
             )


        self.update_sprites()

    def __load_atlas( self ) :
        self.__walk_atlas = PGAtlas(
            "/home/yolo/Workstation/Python/pygame/Chaotic-Kung-Fu-Kid/assets/images/Walk.json" )
        self.__idle_atlas = PGAtlas(
            "/home/yolo/Workstation/Python/pygame/Chaotic-Kung-Fu-Kid/assets/images/Idle.json" )

        self.walk_east_sprites.append( self.__walk_atlas.create_image( "Walk_EAST_0.png" ) )
        self.walk_east_sprites.append( self.__walk_atlas.create_image( "Walk_EAST_1.png" ) )
        self.walk_east_sprites.append( self.__walk_atlas.create_image( "Walk_EAST_2.png" ) )
        self.walk_east_sprites.append( self.__walk_atlas.create_image( "Walk_EAST_3.png" ) )
        self.walk_east_sprites = [Sprite( surface=i ) for i in self.walk_east_sprites]

        self.walk_west_sprites.append( self.__walk_atlas.create_image( "Walk_WEST_0.png" ) )
        self.walk_west_sprites.append( self.__walk_atlas.create_image( "Walk_WEST_1.png" ) )
        self.walk_west_sprites.append( self.__walk_atlas.create_image( "Walk_WEST_2.png" ) )
        self.walk_west_sprites.append( self.__walk_atlas.create_image( "Walk_WEST_3.png" ) )
        self.walk_west_sprites = [Sprite( surface=i ) for i in self.walk_west_sprites]

        self.walk_north_sprites.append( self.__walk_atlas.create_image( "Walk_NORTH_0.png" ) )
        self.walk_north_sprites.append( self.__walk_atlas.create_image( "Walk_NORTH_1.png" ) )
        self.walk_north_sprites.append( self.__walk_atlas.create_image( "Walk_NORTH_2.png" ) )
        self.walk_north_sprites.append( self.__walk_atlas.create_image( "Walk_NORTH_3.png" ) )
        self.walk_north_sprites = [Sprite( surface=i ) for i in self.walk_north_sprites]

        self.walk_south_sprites.append( self.__walk_atlas.create_image( "Walk_SOUTH_0.png" ) )
        self.walk_south_sprites.append( self.__walk_atlas.create_image( "Walk_SOUTH_1.png" ) )
        self.walk_south_sprites.append( self.__walk_atlas.create_image( "Walk_SOUTH_2.png" ) )
        self.walk_south_sprites.append( self.__walk_atlas.create_image( "Walk_SOUTH_3.png" ) )
        self.walk_south_sprites = [Sprite( surface=i ) for i in self.walk_south_sprites]

        self.idle_east_sprites.append( self.__idle_atlas.create_image( "Idle_EAST_0.png" ) )
        self.idle_east_sprites.append( self.__idle_atlas.create_image( "Idle_EAST_1.png" ) )
        self.idle_east_sprites.append( self.__idle_atlas.create_image( "Idle_EAST_2.png" ) )
        self.idle_east_sprites.append( self.__idle_atlas.create_image( "Idle_EAST_3.png" ) )
        self.idle_east_sprites = [Sprite( surface=i ) for i in self.idle_east_sprites]

        self.idle_west_sprites.append( self.__idle_atlas.create_image( "Idle_WEST_0.png" ) )
        self.idle_west_sprites.append( self.__idle_atlas.create_image( "Idle_WEST_1.png" ) )
        self.idle_west_sprites.append( self.__idle_atlas.create_image( "Idle_WEST_2.png" ) )
        self.idle_west_sprites.append( self.__idle_atlas.create_image( "Idle_WEST_3.png" ) )
        self.idle_west_sprites = [Sprite( surface=i ) for i in self.idle_west_sprites]

        self.idle_north_sprites.append( self.__idle_atlas.create_image( "Idle_NORTH_0.png" ) )
        self.idle_north_sprites.append( self.__idle_atlas.create_image( "Idle_NORTH_1.png" ) )
        self.idle_north_sprites.append( self.__idle_atlas.create_image( "Idle_NORTH_2.png" ) )
        self.idle_north_sprites.append( self.__idle_atlas.create_image( "Idle_NORTH_3.png" ) )
        self.idle_north_sprites = [Sprite( surface=i ) for i in self.idle_north_sprites]

        self.idle_south_sprites.append( self.__idle_atlas.create_image( "Idle_SOUTH_0.png" ) )
        self.idle_south_sprites.append( self.__idle_atlas.create_image( "Idle_SOUTH_1.png" ) )
        self.idle_south_sprites.append( self.__idle_atlas.create_image( "Idle_SOUTH_2.png" ) )
        self.idle_south_sprites.append( self.__idle_atlas.create_image( "Idle_SOUTH_3.png" ) )

        self.idle_south_sprites = [Sprite( surface=i ) for i in self.idle_south_sprites]

        self.idle_east_msprite = MSprite( self.idle_east_sprites, 0.5 )
        self.idle_west_msprite = MSprite( self.idle_west_sprites, 0.5 )
        self.idle_north_msprite = MSprite( self.idle_north_sprites, 0.5 )
        self.idle_south_msprite = MSprite( self.idle_south_sprites, 0.5 )

        self.walk_east_msprite = MSprite( self.walk_east_sprites, 0.2 )
        self.walk_west_msprite = MSprite( self.walk_west_sprites, 0.2 )
        self.walk_north_msprite = MSprite( self.walk_north_sprites, 0.2 )
        self.walk_south_msprite = MSprite( self.walk_south_sprites, 0.2 )


    def update_sprites( self ) :
        x_scale = self.rect.height / self.walk_east_sprites[0].get_raw_size().y

        for i in [self.walk_east_msprite, self.walk_north_msprite, self.walk_west_msprite,
                    self.walk_south_msprite] + \
                 [self.idle_east_msprite, self.idle_north_msprite, self.idle_west_msprite,
                    self.idle_south_msprite]:
            i.reset_scale(Pos(x_scale,x_scale))
            i.transform_images()


    def get_center( self ):
        return self.rect.get_pos().join(self.rect.get_size().get_transformed_pos(mult=0.5))

    def set_size( self, size: Pos ) :
        self.rect.get_size().reset( size.x, size.y )

    def move( self ):
        if self.direction == c.NORTH:
            self.rect.y -= self.rect.height * self.move_speed_scale
        elif self.direction == c.SOUTH:
            self.rect.y += self.rect.height * self.move_speed_scale
        elif self.direction == c.EAST:
            self.rect.x += self.rect.width * self.move_speed_scale
        elif self.direction == c.WEST:
            self.rect.x -= self.rect.width * self.move_speed_scale

        if self.rect.x < self.rect.width:
            pass
        if self.rect.y < self.rect.height:
            pass


    def check_events( self ) :

        if self.is_moving:
            self.state = c.WALK
            self.move()
        else:
            self.state = c.IDLE

        target_msprite = self.walk_north_msprite

        if self.state == c.WALK:
            if self.direction == c.SOUTH :
                target_msprite = self.walk_south_msprite
            elif self.direction == c.WEST :
                target_msprite = self.walk_west_msprite
            elif self.direction == c.EAST :
                target_msprite = self.walk_east_msprite

        elif self.state == c.IDLE:
            target_msprite = self.idle_north_msprite
            if self.direction == c.SOUTH :
                target_msprite = self.idle_south_msprite
            elif self.direction == c.WEST :
                target_msprite = self.idle_west_msprite
            elif self.direction == c.EAST :
                target_msprite = self.idle_east_msprite

        target_msprite.check_events()


    def render( self, surface: pg.surface.Surface ) :
        pg.draw.rect( surface, self.color, self.rect )

        target_msprite = self.walk_north_msprite

        if self.state == c.WALK :
            if self.direction == c.SOUTH :
                target_msprite = self.walk_south_msprite
            elif self.direction == c.WEST :
                target_msprite = self.walk_west_msprite
            elif self.direction == c.EAST :
                target_msprite = self.walk_east_msprite

        elif self.state == c.IDLE :
            target_msprite = self.idle_north_msprite
            if self.direction == c.SOUTH :
                target_msprite = self.idle_south_msprite
            elif self.direction == c.WEST :
                target_msprite = self.idle_west_msprite
            elif self.direction == c.EAST :
                target_msprite = self.idle_east_msprite

        target_msprite.render(surface,self.get_center())
