from .Color import Color
from .Enumerator import Enumerator

GLASS = Color(0,0,0,0)
DARK_BLUE = Color(30,30,70)
WOODEN = Color( 70, 40, 40 )

BLACK = Color(0,0,0)
GRAY = Color(127,127,127)
WHITE = Color(255,255,255)

Enumerator.reset("WindowMode")
BLIT_STRETCH = Enumerator.get_next()
REAL_SIZE = Enumerator.get_next()



