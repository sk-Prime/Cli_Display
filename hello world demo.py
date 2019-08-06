import cli_display

text="Hello world of CLI Display!"

frame=cli_display.Frame(25,40)
frame.insert_simple(text,6,11)
frame.update()

while True: #our current frame is static so no need to put frame update
    pass    #inside this loop
