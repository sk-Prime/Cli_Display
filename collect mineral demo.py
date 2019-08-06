import cli_display
try:
    import keyboard
excpet:
    print("install keyboard module, using\npython -m pip install keyboard")
    exit()
from cli_display import sleep,system
from random import randint
class game(object):
    def __init__(self):
        self.y=60
        self.x=35
        self.rate=0.042
        self.sprite="""  ^\n<FlY>\n ! !"""
        self.m_f=0
        self.mineral=["+","+","+",":",":",":",".",".",".","-","-","-"]
        self.m_posx=20
        self.m_posy=20

        self.l_sp=self.sprite.count("\n")
        self.r_pos_x=0
        self.r_pos_y=0
        self.rocket_frame=cli_display.Frame(self.x,self.y)
        self.point=0
        self.time_control=0
    def control_input(self):
        if keyboard.is_pressed('up'):
            self.r_pos_y-=1
            if self.r_pos_y<0:
                self.r_pos_y=0
        elif keyboard.is_pressed('down'):
            self.r_pos_y+=1
            if self.r_pos_y>(self.x-self.l_sp-2):
                self.r_pos_y=self.x-self.l_sp-2
        elif keyboard.is_pressed('right'):
            self.r_pos_x+=1
            if self.r_pos_x>(self.y-5):
                self.r_pos_x=self.y-5
        elif keyboard.is_pressed('left'):
            self.r_pos_x-=1
            if self.r_pos_x<0:
                self.r_pos_x=0

    def collison_detect(self):
        mpos=[self.m_posx,self.m_posy]
        rx=self.r_pos_x
        ry=self.r_pos_y
        field=[[rx-2,ry],[rx,ry+1],[rx+1,ry+1],
        [rx+2,ry+1],[rx+3,ry+1],[rx+4,ry+1],
        [rx+1,ry+2],[rx+3,ry+2]]
        if mpos in field:
            self.randomize_mineral()
            self.point+=1
            print("\a")

    def randomize_mineral(self):
        self.m_posx=randint(5,self.y-5)
        self.m_posy=randint(5,self.x-5)


    def frame_control(self):
        while True:
            self.control_input()
            self.rocket_frame.insert_simple(self.sprite+"\n  %d"%self.point,self.r_pos_x,self.r_pos_y)
            if self.time_control==50:
                self.randomize_mineral()
                self.time_control=0
            self.rocket_frame.insert_simple(self.mineral[self.m_f],self.m_posx,self.m_posy)
            self.rocket_frame.update()
            self.collison_detect()
            self.rocket_frame.wait(self.rate)
            self.rocket_frame.clear_frame()
            #self.rocket_frame.cmd_command() #win7 uncomment
            self.time_control+=1
            self.m_f+=1
            if self.m_f==12:
                self.m_f=0
    def run(self):
        self.frame_control()

if __name__=="__main__":
    rocket=game()
    rocket.run()

