big_num=["""  ****  \n ****** \n***  ***\n**   ***\n** *****\n***** **\n***   **\n***  ***\n ****** \n  ****  """,
         """  ***  \n*****  \n** **  \n   **  \n   **  \n   **  \n   **  \n   **  \n*******\n*******\n        """,
         """ ***** \n*******\n *   **\n     **\n    ***\n    ** \n  ***  \n ***   \n*******\n*******\n        """,
         """*****  \n****** \n    ** \n    ** \n ****  \n ***** \n     **\n     **\n*******\n*****  \n        """,
         """    *** \n   **** \n  ** ** \n  ** ** \n **  ** \n**   ** \n********\n********\n     ** \n     ** """,
         """****** \n****** \n**     \n**     \n****** \n*******\n     **\n     **\n****** \n*****  \n        """,
         """  **** \n ***** \n***    \n**     \n** *** \n*******\n**   **\n**   **\n ******\n  **** \n        """,
         """*******\n*******\n     **\n    ** \n    ** \n   **  \n   **  \n  **   \n  **   \n **    \n        """,
         """ ***** \n*******\n**   **\n*** ***\n ***** \n ***** \n**   **\n**   **\n*******\n ***** \n        """,
         """ ****  \n****** \n**   **\n**   **\n*******\n *** **\n     **\n    ***\n ***** \n ****  \n        """,
         """       \n       \n  ***  \n  ***  \n  ***  \n       \n  ***  \n  ***  \n  ***  \n       \n        """]


from datetime import datetime
import cli_display

def text_make():
    now = datetime.now()
    ctime = now.strftime("%I:%M:%S")
    big_clock=""
    for i in range(10):
        for n in ctime:
            if n==":":
               big_clock="%s%s"%(big_clock,big_num[10].split("\n")[i]+"  ")
            else:
                big_clock="%s%s"%(big_clock,big_num[int(n)].split("\n")[i]+"  ")
        big_clock+="\n"
    return big_clock



clock_frame=cli_display.Frame(10,80)
clock_frame.cmd_command("color 0c")
while True:
    clock_text=text_make()
    clock_frame.insert_simple(clock_text)
    clock_frame.update()
    clock_frame.wait(0.09)
