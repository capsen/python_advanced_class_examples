import pgzrun
from pgzhelper import *
from sprite import *

WIDTH = 800
HEIGHT = 600
elements = []
current_frame=0

backdrops = Actor("arctic")
backdrops.images=["arctic", "baseball", "canyon"]

next_btn = Sprite("next_up")
next_btn.topleft=(480, 480)
next_btn.scale=0.3
elements.append(next_btn)


back_btn = Sprite("prev_up")
back_btn.topleft=(80, 480)
back_btn.scale=0.3
elements.append(back_btn)


abby = Sprite("abby-a")
abby.topleft = (5, 280)
abby.scale=0.5
elements.append(abby)


devin = Sprite("devin-a")
devin.topleft = (640, 280)
devin.scale=0.5
elements.append(devin)


def btn_clicked():
    backdrops.next_image()

def draw():
    screen.clear()
    backdrops.draw()
    for element in elements:
        if element.show:
            element.draw()

def update():
    pass

def frame_changed():
    match current_frame:
        case 0:
            print("frame:", current_frame)
            abby.show=True
        case 1:
            abby.show=False
        case 2:
            print("frame:", current_frame)
            abby.show=True
        case _:
            print("frame:", current_frame)
            abby.show=False

    if current_frame>0:
        back_btn.show=True
    else:
        back_btn.show=False
    


def next_frame():
    global current_frame
    current_frame += 1
    frame_changed()

def prev_frame():
    global current_frame
    current_frame -= 1
    frame_changed()

def on_mouse_down(pos):
    if next_btn.collidepoint(pos) and next_btn.show:
        next_btn.image="next_down"
    if back_btn.collidepoint(pos) and back_btn.show:
        back_btn.image="prev_down"

def on_mouse_up(pos):
    if next_btn.collidepoint(pos) and next_btn.show:
        next_btn.image="next_up"
        next_frame()
    if back_btn.collidepoint(pos) and back_btn.show:
        back_btn.image="prev_up"
        prev_frame()

frame_changed()
pgzrun.go()

#Ctrl + C to stop the program