import pgzrun
import pgzero
from pgzhelper import *
from sprite import *
from button import Button
from quizcomponent import *

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

quiz = Quiz("quiz_questions.json", finish=next_frame)

# start_btn = Button("start", (400, 300), start)
# start_btn.scale=0.3
# start_btn.show=False
# elements.append(start_btn)
# btns.append(start_btn)

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

    screen.draw.text(str(current_frame),pos=(10,10))
    for element in elements:
        if element.show:
            element.draw()
    
    quiz.draw()

def update():
    pass

def frame_changed():
    match current_frame:
        case 1:
            next_btn.show=False
            back_btn.show=False
            abby.show=True
            abby.message="Hello Devin, It's a nice day, how are you?"
            sounds.hello_devin.play()
            clock.schedule(next_frame, 3)
        case 2:
            abby.message=""
            devin.show=True
            devin.message="I am good, thank you."
            sounds.iamgood.play()
            clock.schedule(next_frame, 3)
        case 3:
            abby.message="Let's go out and play."
            devin.message=""
            sounds.letgoout.play()
            clock.schedule(next_frame, 3)
        case 4:
            abby.message=""
            devin.message="OK"
            sounds.ok.play()
            clock.schedule(next_frame, 1)
        case 5:
            abby.message=""
            devin.message=""
            animate(abby, pos=(abby.pos[0]+10, abby.pos[1]-20), duration=1)
            animate(devin, pos=(devin.pos[0]-600, devin.pos[1]), duration=1)
            devin.image="devin-b"
            clock.schedule(next_frame, 1.5)
        case 6:
            abby.message="Let's have a quiz game."
            clock.schedule(next_frame, 1)
        case 7:
            backdrops.image="bg1"
            abby.message=""
            abby.show=False
            devin.show=False
            quiz.load_quiz()
        case 8:
            backdrops.image="boardwalk"
            abby.message="Well done, Let's go to cinema."
            abby.show=True
            devin.show=True
            quiz.show=False
        case _:
            abby.message=""
            devin.message=""
            

    # if current_frame>0:
    #     back_btn.show=True
    # else:
    #     back_btn.show=False

    if current_frame>4 and current_frame < 7:
        backdrops.image="boardwalk"


def on_mouse_down(pos):
    for btnitem in btns:
        btnitem.on_mouse_down(pos)
    quiz.on_mouse_down(pos)

def on_mouse_up(pos):
    for btnitem in btns:
        btnitem.on_mouse_up(pos)
    quiz.on_mouse_up(pos)

frame_changed()
pgzrun.go()

#Ctrl + C to stop the program