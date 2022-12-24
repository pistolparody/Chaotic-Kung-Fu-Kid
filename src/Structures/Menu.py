import pygame as pg

from . import Constants
from .Pos import Pos
from .Rect import Rect
from .Color import Color

from .TextHolder import TextHolder
from .TextBox import TextBox
from .Enums import Payams


class Menu :

    def __init__( self, surface_size: Pos, surface_pos: Pos = Pos( 0, 0 ) ) :
        self.__surface_pos = surface_pos
        self.__surface_size = surface_size
        self.__surface = pg.surface.Surface( self.__surface_size.get_tuple() ).convert_alpha()

        self.__surface_color = Color( 0, 0, 0, 0 )

        text_box_size = self.__surface_size.get_transformed_pos( mult=0.5 )

        text = TextHolder(Payams.LongText,pg.font.Font(None,30),
                        text_box_size.x )


        self.text_box = TextBox(
            Rect.fromPos( Pos( 0, 0 ),  text_box_size) ,
                        text)

        t_b_rect = self.text_box.get_rect()



        self.text_box.get_rect().reset_pos(

            self.__surface_size.x / 2 - text_box_size.x / 2
            ,
            self.__surface_size.y / 2 - text_box_size.y / 2

        )




    def set_color( self, color: Color ) :
        self.__surface_color = color


    def get_events( self, event_list=None ) :
        if event_list is None : event_list = list()

        if len( event_list ) == 0 : event_list = pg.event.get()

        for i in event_list :
            pass


    def check_events( self ) :
        pass


    def render( self, surface: pg.surface.Surface ) :
        self.__surface.fill( self.__surface_color.get_tuple() )
        self.text_box.render( self.__surface )

        surface.blit( self.__surface, self.__surface_pos.get_tuple() )


    def run( self, surface: pg.surface.Surface, event_list: list = None ) :
        self.get_events( event_list )
        self.check_events()
        self.render( surface )

