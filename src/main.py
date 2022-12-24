import pygame as pg
import time

from Structures.Window import Window
from Structures.Pos import Pos
from Structures.Color import Color
from Structures.Menu import Menu
from Structures.TextBox import TextBox
from Structures.TextHolder import TextHolder
from Structures.Rect import Rect

bg = Color(150,150,255)

pg.init()

window = Window(Pos(1000,725),Pos(800,600),"Chaotic Kung-Fu King",0)
menu = Menu(window.get_mask_size())
textHolder = TextHolder("What's up?",pg.font.Font(None,10),500)

textBox = TextBox(Rect(100,100,200,200),textHolder)



frames = 0
t = time.time()

while window.is_running:
    frames += 1
    event_list = pg.event.get()
    menu.run(window.get_mask(),event_list)
    # textBox.render(window.get_mask())
    window.run(event_list)
    window.get_mask().fill(bg)

    if frames >= 60:
        frames = 0
        t = time.time()