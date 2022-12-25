import pygame as pg

class Game:
    def __init__( self ):
        self.counter = 0
        pass

    def next( self ):
        self.counter+=1


    def get_events( self, event_list:list = None):
        if event_list is None: event_list = pg.event.get()

        for i in event_list:
            pass

    def check_events( self ):
        pass

    def render( self , surface:pg.surface.Surface):
        pass