class Pos :
    def __init__( self, x: float, y: float ) :
        self.x = x
        self.y = y

    def __str__( self ) :
        return "[PosObject : ({},{})]".format( self.x, self.y )

    def copy( self ) :
        return Pos( self.x, self.y )

    def reset( self, new_x: float = 0, new_y: float = 0 ) :
        self.x, self.y = new_x, new_y

        return self

    def reset_by_tuple( self, pos: tuple[float, float] ) :
        self.x, self.y = pos
        return self

    def get_tuple( self ) :
        return self.x, self.y

    def transform( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        if not sum_first :
            self.x *= mult
            self.x += Sum
            self.y *= mult
            self.y += Sum
        else :
            self.x += Sum
            self.x *= mult
            self.y += Sum
            self.y *= mult

        return self


    def get_transformed_pos( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        return Pos( self.x, self.y ).transform( Sum, mult, sum_first )

    def get_transformed_tuple( self, Sum: float = 0, mult: float = 1, sum_first: bool = False ) :
        return Pos( self.x, self.y ).transform( Sum, mult, sum_first ).get_tuple()

    def join( self, pos ) :
        return Pos( self.x + pos.x, self.y + pos.y )