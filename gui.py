import os
import sys
from pathlib import Path
import clipboard

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess

def copy2clip(txt):
    cmd='echo '+str(txt).strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


class Subject():
    def __init__(self, code, passw=''):
        self.code = code
        self.passw = passw

    def copyCode(self):
        copy2clip(self.code)

    def copyPw(self):
        copy2clip(self.passw)
    




mat = Subject(code='8955489281', passw='880425')
sjl = Subject(code='8955489281', passw='880425')
tsv = Subject(code='967 9747 5467', passw='TSV')
dej = Subject(code='740 2084 9957', passw='DEJ')
anj = Subject(code='4360045986')
che = Subject(code='410 843 6589', passw='sktKt1')
geg = Subject(code='931 3133 4145', passw='GEG')
nej = Subject(code='447 266 1286', passw='7AgZ7U')

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


# def copy2clip(txt):
#     cmd='echo '+txt.strip()+'|clip'
#     return subprocess.check_call(cmd, shell=True)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title('zoom hodiny')

window.bind("<Key> R",os.system(r'start C:\Users\vikto\AppData\Roaming\Zoom\bin\Zoom.exe'))
window.iconphoto(True, PhotoImage(file = r"C:\Users\vikto\Documents\AHOJ\build\icon.png"))


window.geometry("928x369")
window.configure(bg = "#FFFFFF")

def copy(text):
    window.clipboard_clear()
    window.clipboard_append(text)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 369,
    width = 928,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    928.0,
    369.0,
    fill="#4B4D55",
    outline="")

canvas.create_rectangle(
    194.0,
    123.0,
    317.0,
    173.0,
    fill="#000000",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.bind('<Button-3>', lambda x:[window.clipboard_clear(),window.clipboard_append(anj.passw)])
button_1.bind('<Button-1>', lambda x:[window.clipboard_clear(),window.clipboard_append(anj.code)])
button_1.place(
    x=611.0,
    y=123.0,
    width=123.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.bind('<Button-3>', lambda x:[window.clipboard_clear(),window.clipboard_append(che.passw)])
button_2.bind('<Button-1>', lambda x:[window.clipboard_clear(),window.clipboard_append(che.code)])
button_2.place(
    x=472.0,
    y=123.0,
    width=123.0,
    height=50.0
)



button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:print('3'),
    relief="flat"
)
button_3.bind('<Button-3>', lambda x:[window.clipboard_clear(),window.clipboard_append(sjl.passw)])
button_3.bind('<Button-1>', lambda x:[window.clipboard_clear(),window.clipboard_append(sjl.code)])
button_3.place(
    x=333.0,
    y=123.0,
    width=123.0,
    height=50.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_8.bind('<Button-3>', lambda x:[window.clipboard_clear(),window.clipboard_append(sjl.passw)])
button_8.bind('<Button-1>', lambda x:[window.clipboard_clear(),window.clipboard_append(sjl.code)])
button_8.place(
    x=194.0,
    y=123.0,
    width=123.0,
    height=50.0
)







button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.bind('<Button-3>', lambda x:[window.clipboard_clear(),window.clipboard_append(tsv.passw)])
button_4.bind('<Button-1>', lambda x:[window.clipboard_clear(),window.clipboard_append(tsv.code)])
button_4.place(
    x=194.0,
    y=195.0,
    width=123.0,
    height=50.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.bind('<Button-3>', lambda x:[window.clipboard_clear(),window.clipboard_append(dej.passw)])
button_5.bind('<Button-1>', lambda x:[window.clipboard_clear(),window.clipboard_append(dej.code)])
button_5.place(
    x=611.0,
    y=195.0,
    width=123.0,
    height=50.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.bind('<Button-3>', lambda x:[window.clipboard_clear(),window.clipboard_append(geg.passw)])
button_6.bind('<Button-1>', lambda x:[window.clipboard_clear(),window.clipboard_append(geg.code)])
button_6.place(
    x=472.0,
    y=195.0,
    width=123.0,
    height=50.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.bind('<Button-3>', lambda x:[window.clipboard_clear(),window.clipboard_append(nej.passw)])
button_7.bind('<Button-1>', lambda x:[window.clipboard_clear(),window.clipboard_append(nej.code)])
button_7.place(
    x=333.0,
    y=195.0,
    width=123.0,
    height=50.0
)

canvas.create_text(
    356.0,
    29.0,
    anchor="nw",
    text="HODINA",
    fill="#FFFFFF",
    font=("UnicaOne Regular", 72 * -1)
)
window.resizable(False, False)
window.mainloop()
