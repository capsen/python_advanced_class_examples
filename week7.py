import pygame
import pgzrun
from pgzhelper import *

mod = sys.modules['__main__']

class Option(Actor):
    def __init__(self, optionimage, optiontext, pos=POS_TOPLEFT, callback=None, show=True):
        super().__init__(optionimage + '_up', pos)
        self.optionimage = optionimage
        self.callback = callback
        self.optiontext = optiontext
        self.show=show

    def on_mouse_down(self, pos):
        if self.show and self.collidepoint(pos):
            self.image=self.optionimage + "_down"

    def on_mouse_up(self, pos):
        if self.show and self.collidepoint(pos):
            self.image=self.optionimage + "_up"
            if self.callback:
                self.callback()

    def draw(self):
        if self.show:
            super().draw()
            self.drawtext()
    
    def drawtext(self):
        topleft=self.topleft
        x=topleft[0]
        y=topleft[1]
        mod.screen.draw.textbox(self.optiontext, (x+self.width/11, y+self.height/8, self.width-self.width/11*2, self.height-self.height/8*2))


# below is the test code
WIDTH = 800
HEIGHT = 600

backdrops = Actor("bg1")
backdrops.scale = 0.5
backdrops.pos=(400,300)

op1 = Option("option", "A. Tom", (200, 400))
op1.scale=0.4

op2 = Option("option", "B. Jacky", (600, 400))
op2.scale=0.4

op3 = Option("option", "C. Sicong", (200, 480))
op3.scale=0.4

op4 = Option("option", "D. Capsen", (600, 480))
op4.scale=0.4

question = Option("question", "Do you know who is the best person? Choose one.", (400, 200))
question.scale=0.6

def draw():
    screen.clear()
    backdrops.draw()
    op1.draw()
    op2.draw()
    op3.draw()
    op4.draw()
    question.draw()


def on_mouse_down(pos):
    op1.on_mouse_down(pos)
    op2.on_mouse_down(pos)
    op3.on_mouse_down(pos)
    op4.on_mouse_down(pos)


def on_mouse_up(pos):
    op1.on_mouse_up(pos)
    op2.on_mouse_up(pos)
    op3.on_mouse_up(pos)
    op4.on_mouse_up(pos)

pgzrun.go()