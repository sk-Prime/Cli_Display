from time import sleep
from os import system

class Frame(object):
    def __init__(self,frame_height=25,frame_width=40,bg=" "):
        self.frame=""
        self.f_y=frame_height
        self.f_x=frame_width
        self.bg=bg
        self.clear_frame()
        self._set_cmd_window()
    def clear_frame(self):
        self.frame=self.bg*(self.f_x*self.f_y)

    def insert_simple(self, content="",pos_x=0,pos_y=0):
        content_list=content.split("\n")
        for item in content_list:
            length=len(item)
            begin=pos_y*self.f_x+pos_x
            end=begin+length
            self.frame="%s%s%s"%(self.frame[0:begin],item,self.frame[end:])
            pos_y+=1
    def _set_cmd_window(self):
        system("mode con:cols=%d lines=%d"%(self.f_x,self.f_y+2))
    def update(self,mode=""):
        print(self.frame+mode)

    def wait(self,time):
        sleep(time)
    def cmd_command(self,d="cls"):
        system(d)




if __name__=="__main__":
    height=25
    width=40
    frame_rate=0.09
    sprite="""xx\nxx"""
    frame=Frame(height,width)
    posy=0
    while True:
        frame.insert_simple(sprite,pos_y=posy)
        frame.update()
        frame.wait(frame_rate)
        frame.clear_frame()
        frame.cmd_command()
        posy+=1
        if posy==17:
            posy=0
