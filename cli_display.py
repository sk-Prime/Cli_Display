from time import sleep
from os import system
import platform

class Frame(object):
    def __init__(self,frame_height=25,frame_width=40,bg=" "):
        self.frame=""
        self.f_y=frame_height
        self.f_x=frame_width    #command prompt height and width
        self.bg=bg              #current background is transparent
        self.clear_frame()
        self.sysName=platform.system()

        self._set_window_size()  #resize cmd window by given height and width


    def clear_frame(self):
        self.frame=self.bg*(self.f_x*self.f_y) #filling cmd window with space
        #otherwise (unwanted) objects of previous frame will appear again.

    def insert_simple(self, content="",pos_x=0,pos_y=0): #this function will
        content_list=content.split("\n")                 #insert given content
        for item in content_list:                        #in self.frame
            length=len(item)                             #any modification need
            begin=pos_y*self.f_x+pos_x                   #to be done in this var
            end=begin+length
            self.frame="%s%s%s"%(self.frame[0:begin],item,self.frame[end:])
            pos_y+=1

    def update(self,mode=""):
        print("%s%s"%(self.frame,mode)) #printing self.frame

    def wait(self,time):
        sleep(time)

    def bounding_box(self,sprite,cpos=()): #current position of the sprite
        box=set()
        old_x=cpos[0]
        x,y=cpos #position of sprite in the frame
        for ch in sprite:
            if ch=="\n": #newline means y increase
                y+=1
                x=old_x #x begins
            elif ch==self.bg: #self.bg is transparent and will not collide
                x+=1      #so ignoring
            else:
                box.add((x,y))
                x+=1
        return box

    def cmd_clear_nl(self): #clear cmd using newline
        print("\n"*self.f_y)

    def cmd_command(self,c): #sometime, terminal needs to be cleared. this func
        system(c)           #can be used for that

    def _set_window_size(self): #resize cmd window
        if self.sysName=="Windows":
            system("mode con:cols=%d lines=%d"%(self.f_x,self.f_y+2))
        elif self.sysName=="Linux":
            system("printf '\e[8;%d;%dt'"%(self.f_y,self.f_x))



if __name__=="__main__":
    text="Hello world animation :O"
    frame = Frame()

    def move_maker(text):
        for i in range(len(text)):
            for y in range(0,6):
                yield "%s%s%s%s%s"%(text[:i],(" "*(5-y)),text[i],(" "*y),text[i+1:])

    while True:
        for string in move_maker(text):
            frame.insert_simple(string,6,11)
            frame.update()
            frame.wait(0.05)
            frame.clear_frame()

