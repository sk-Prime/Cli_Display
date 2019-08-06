import cli_display

text="Hello world animation :O"
tlen=len(text)

def move_maker(text):
    for i in range(tlen):
        for y in range(0,6):
            yield "%s%s%s%s%s"%(text[:i],(" "*(5-y)),text[i],(" "*y),text[i+1:])

frame=cli_display.Frame()

while True:
    for x in move_maker(text):
        frame.insert_simple(x,6,11)
        frame.update()
        frame.wait(0.03)
        frame.clear_frame()
        #frame.cmd_command("cls") #if win7 uncomment
