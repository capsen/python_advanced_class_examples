import pygame
import json
from pgzhelper import *

mod = sys.modules['__main__']

class Option(Actor):
    def __init__(self, optionimage, optiontext, order="", pos=POS_TOPLEFT, callback=None, show=True):
        super().__init__(optionimage + '_up', pos)
        self.optionimage = optionimage
        self.callback = callback
        self.optiontext = optiontext
        self.show=show
        self.order=order

    def on_mouse_down(self, pos):
        if self.show and self.collidepoint(pos):
            self.image=self.optionimage + "_down"

    def on_mouse_up(self, pos):
        if self.show and self.collidepoint(pos):
            self.image=self.optionimage + "_up"
            if self.callback:
                self.callback(self.optiontext)

    def draw(self):
        if self.show:
            super().draw()
            self.drawtext()
    
    def drawtext(self):
        topleft=self.topleft
        x=topleft[0]
        y=topleft[1]
        mod.screen.draw.textbox(self.order+self.optiontext, (x+self.width/11, y+self.height/8, self.width-self.width/11*2, self.height-self.height/8*2))


class Question():
    def __init__(self, question, callback=None):
        self.question = question
        self.current_answer=None
        self.callback = callback
        self.questionUI = Option("question", question["description"], pos=(400, 200))
        self.questionUI.scale=0.6
        self.op1 = Option("option", str(question["options"][0]), order="A. ", callback=self.option_clicked, pos=(200, 400))
        self.op1.scale=0.4
        self.op2 = Option("option", str(question["options"][1]), order="B. ", callback=self.option_clicked, pos=(600, 400))
        self.op2.scale=0.4
        self.op3 = Option("option", str(question["options"][2]), order="C. ", callback=self.option_clicked, pos=(200, 480))
        self.op3.scale=0.4
        self.op4 = Option("option", str(question["options"][3]), order="D. ", callback=self.option_clicked, pos=(600, 480))
        self.op4.scale=0.4
        
    
    def option_clicked(self, option_value):
        self.current_answer=option_value
        print(option_value)
        self.slide([self.questionUI, self.op1, self.op2, self.op3, self.op4], 0.5, False)
        mod.clock.schedule(self.callback, 0.5)
        

    def start_entry(self):
        self.slide([self.questionUI, self.op1, self.op2, self.op3, self.op4], 0.5, True)
    
    def slide(self, objs, duration, isEntry):
        for obj in objs:
            end=obj.pos if isEntry else (obj.pos[0]-800,obj.pos[1])
            start=(obj.pos[0]+800,obj.pos[1]) if isEntry else obj.pos
            obj.pos=start
            mod.animate(obj, pos=end, duration=duration)
    
    def draw(self):
        self.questionUI.draw()
        self.op1.draw()
        self.op2.draw()
        self.op3.draw()
        self.op4.draw()
    
    def on_mouse_down(self, pos):
        self.op1.on_mouse_down(pos)
        self.op2.on_mouse_down(pos)
        self.op3.on_mouse_down(pos)
        self.op4.on_mouse_down(pos)

    def on_mouse_up(self, pos):
        self.op1.on_mouse_up(pos)
        self.op2.on_mouse_up(pos)
        self.op3.on_mouse_up(pos)
        self.op4.on_mouse_up(pos)

class Quiz():
    def __init__(self, quizpath, finish=None):
        self.show=False
        self.current_question=0
        self.questions=[]
        self.quizpath=quizpath
        self.finish=finish
        self.end_btn = Option("option", "Close", callback=self.end_quiz, pos=(200, 400))
        self.end_btn.show = False
        self.retry_btn = Option("option", "Retry", callback=self.reload, pos=(600, 400))
        self.retry_btn.show = False
        self.retry_btn.scale=0.4
        self.end_btn.scale=0.4
        self.quiz_end = Option("question", "", pos=(400, 200))
        self.quiz_end.show = False
        self.quiz_end.scale=0.6
    
    def end_quiz(self, text):
        if self.finish:
            self.finish()

    def load_quiz(self):
        with open(self.quizpath, 'r') as f:
            # load the data from the file
            quiz_data = json.load(f)

        self.current_question=0
        self.questions=[]
        self.quiz_end.show = False
        self.end_btn.show = False
        self.retry_btn.show = False

        for question in quiz_data["questions"]:
            q = Question(question, callback=self.question_answered)
            self.questions.append(q)
        self.show=True
        self.questions[self.current_question].start_entry()

    def question_answered(self):
        if(self.current_question<len(self.questions)-1):
            self.current_question+=1
            self.questions[self.current_question].start_entry()
        else:
            self.quiz_result = 0
            for q in self.questions:
                if q.current_answer == str(q.question["correct_answer"]):
                    print("True")
                    self.quiz_result +=1
                else:
                    print("False")
            self.quiz_end.optiontext= "Congratulations! You have passed the test." if self.quiz_result>len(self.questions)/2 else "Sorry! You didn't passed the test, please try again"
            self.quiz_end.show = True
            self.end_btn.show = True
            self.retry_btn.show = True
    
    def reload(self, text):
        print("loaded")
        self.load_quiz()

    def draw(self):
        if self.show:
            self.questions[self.current_question].draw()
            self.quiz_end.draw()
            self.end_btn.draw()
            self.retry_btn.draw()

    def on_mouse_down(self, pos):
        if len(self.questions)>self.current_question:
            self.questions[self.current_question].on_mouse_down(pos)
        self.end_btn.on_mouse_down(pos)
        self.retry_btn.on_mouse_down(pos)

    def on_mouse_up(self, pos):
        if len(self.questions)>self.current_question:
            self.questions[self.current_question].on_mouse_up(pos)
        self.end_btn.on_mouse_up(pos)
        self.retry_btn.on_mouse_up(pos)

