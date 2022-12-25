import pygame as pg
import time

from Structures.Window import Window
from Structures.Pos import Pos
from Structures.Color import Color
from Structures.Menu import Menu
from Structures.TextBox import TextBox
from Structures.TextHolder import TextHolder
from Structures.Rect import Rect
from Structures.Page import Page

bg = Color(150,150,255)

pg.init()

window = Window(Pos(1000,725),Pos(800,600),"Chaotic Kung-Fu King",0)
menu = Menu(window.get_mask_size())
textHolder = TextHolder("What's up?",pg.font.Font(None,30))
textBox = TextBox(Rect(100,100,600,50),textHolder)
textBox0 = TextBox(Rect(100,100,600,50),textHolder)
textBox1 = TextBox(Rect(100,100,600,50),textHolder)

textBox.centralize_text()
textBox.update_surface()

page = Page((400,300),height_step=100)
page.addTextBox(textBox)
page.addTextBox(textBox0)
page.addTextBox(textBox1)

page.update_page()



frames = 0
t = time.time()

while window.is_running:
    frames += 1
    event_list = pg.event.get()
    menu.run(window.get_mask(),event_list)

    window.run(event_list)
    window.get_mask().fill(bg)
    page.render(window.get_mask())

    if frames >= 60:
        frames = 0
        t = time.time()