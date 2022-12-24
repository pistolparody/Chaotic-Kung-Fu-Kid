import pygame as pg
from .Pos import Pos

class Sprite:
    def __init__(self,path:str):
        self.path = path
        self.__raw_image = pg.image.load(path)

        self.auto_transform = False

        self.__x_flip = False
        self.__y_flip = False
        self.__angle = 0
        self.__scale = Pos(0,0)
        self.__scale.x , self.__scale.y = self.__raw_image.get_size()

        self.__transformed_image = self.__raw_image
        self.transform_image()

    def reload( self ,path:str ):
        self.path = path
        self.__raw_image = pg.image.load( path )
        self.transform_image()

    def get_raw_image( self ):
        return self.__raw_image

    def get_transformed_image( self ):
        return self.__transformed_image

    def get_flips( self ):
        return self.__x_flip,self.__y_flip

    def get_angle( self ):
        return self.__angle

    def get_scale( self ):
        return self.__scale


    def reset_flips( self ,x_flip:bool=False,y_flip:bool=False) :
        self.__x_flip,self.__y_flip = x_flip,y_flip
        if self.auto_transform: self.transform_image()

        return self


    def reset_angle( self , angle:float=0) :
        self.__angle = angle
        if self.auto_transform : self.transform_image()

        return self


    def reset_scale( self , scale:Pos=None) :
        if scale is None:
            scale = self.__raw_image.get_size()
            self.__scale.reset_by_tuple(scale)
        else:
            self.__scale = scale

        if self.auto_transform : self.transform_image()

        return self


    def transform_image( self ):
        self.__transformed_image = self.__raw_image
        if any([self.__x_flip,self.__y_flip]):
            self.__transformed_image = pg.transform.flip(
                self.__transformed_image,self.__x_flip,self.__y_flip)

        if self.__angle != 0:
            self.__transformed_image = pg.transform.rotate(self.__transformed_image,self.__angle)

        if self.__scale.x != self.__raw_image.get_width() and \
                    self.__scale.y != self.__raw_image.get_height():

            self.__transformed_image = pg.transform.scale(
                self.__transformed_image,self.__scale.get_tuple())

        return self


    def render( self , surface:pg.surface.Surface , top_left_pos:Pos):
        surface.blit(self.__transformed_image,top_left_pos.get_tuple())
