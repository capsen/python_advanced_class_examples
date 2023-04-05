import pgzrun
from pgzhelper import *
from sprite import *
from button import Button

WIDTH = 800
HEIGHT = 600
elements = []
btns = []
current_frame=0

#---------- custom functions -----------------
def next_frame():
    global current_frame
    current_frame += 1
    frame_changed()

def prev_frame():
    global current_frame
    current_frame -= 1
    frame_changed()

def start():
    start_btn.show=False
    print("code started")
#---------- elements

backdrops = Actor("arctic")
backdrops.images=["arctic", "baseball", "canyon"]

next_btn = Button("next", (550, 520), next_frame)
next_btn.scale=0.3
elements.append(next_btn)
btns.append(next_btn)

back_btn = Button("prev", (150, 520), prev_frame)
back_btn.scale=0.3
back_btn.show=False
elements.append(back_btn)
btns.append(back_btn)

start_btn = Button("start", (400, 300), start)
start_btn.scale=0.3
start_btn.show=False
elements.append(start_btn)
btns.append(start_btn)

abby = Sprite("abby-a")
abby.topleft = (5, 280)
abby.scale=0.5
elements.append(abby)

devin = Sprite("devin-a")
devin.topleft = (640, 280)
devin.scale=0.5
elements.append(devin)

def draw():
    screen.clear()
    backdrops.draw()
    for element in elements:
        element.draw()

def update():
    pass

def frame_changed():
    
    match current_frame:
        case 1:
            next_btn.show=False
            abby.show=True
            abby.message="Hello Devin, how are you?"
            sounds.hello.play()
            clock.schedule(next_frame, sounds.hello.get_length()+0.5)
        case 2:
            abby.message=""
            devin.show=True
            devin.message="I am good, thank you."
            sounds.iamgood.play()
            clock.schedule(next_frame, 3)
        case 3:
            abby.message="Let's go out and play."
            devin.message=""
            sounds.letsgoout.play()
            clock.schedule(next_frame, 3)
        case 4:
            abby.message=""
            devin.message="OK"
            sounds.ok.play()
            clock.schedule(next_frame, 1)
        case 5:
            abby.message=""
            devin.message=""
            animate(abby, pos=(300, 400), duration=1)
            animate(devin, pos=(400, 400), duration=1)
        case _:
            abby.message=""
            devin.message=""

    # if current_frame>0:
    #     back_btn.show=True
    # else:
    #     back_btn.show=False

    if current_frame>4:
        backdrops.image="canyon"


def on_mouse_down(pos):
    for btnitem in btns:
        btnitem.on_mouse_down(pos)

def on_mouse_up(pos):
    for btnitem in btns:
        btnitem.on_mouse_up(pos)

frame_changed()
pgzrun.go()

#Ctrl + C to stop the program