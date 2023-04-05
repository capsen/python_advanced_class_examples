import pgzrun
from pgzhelper import *

WIDTH = 800
HEIGHT = 600

backdrops = Actor("arctic")
backdrops.images=["arctic", "baseball", "canyon"]

btn = Actor("clickup")
btn.center=(WIDTH/2, HEIGHT/2)
btn.scale=0.2

def btn_clicked():
    backdrops.next_image()

def draw():
    screen.clear()
    backdrops.draw()
    btn.draw()

def update():
    pass

def on_mouse_down(pos):
    if btn.collidepoint(pos):
        btn.image="clickdown"

def on_mouse_up(pos):
    if btn.collidepoint(pos):
        btn.image="clickup"
        btn_clicked()

pgzrun.go()

#Ctrl + C to stop the program