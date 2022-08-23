from tkinter import *
from PIL import ImageTk, Image
import time
import os
import requests
from io import BytesIO

# declare the window
win = Tk()
#icon stuff
responseico = requests.get("https://cdn.discordapp.com/attachments/912359331817717841/1011668097826037790/image-removebg-preview_20.png")
ico = Image.open(BytesIO(responseico.content))
photo = ImageTk.PhotoImage(ico)
win.wm_iconphoto(True, photo)

# set window title
win.title("windws 39 udate")
#idk why i added this
user = os.getlogin()

def create():
    wasd = Toplevel(win)
    wasd.geometry('1440x900')
    wasd.title("lfao nob computar brik")
    frame2 = Frame(wasd, width=1440, height=900)
    frame2.pack()
    frame2.place(anchor='nw', relx=0, rely=0)
    response = requests.get("https://cdn.discordapp.com/attachments/979393895500763186/1011400678981259435/ur_pc_bicked_skull.png")
    img2 = ImageTk.PhotoImage(Image.open(BytesIO(response.content))) 
    label2 = Label(frame2, image = img2)
    label2.pack()
    label2.photo = img2
    wasd.configure(bg="black")
    wasd.attributes('-fullscreen', True)

win.geometry('850x500')

btn = Button(win, text = 'istall', command = create, height=2, width=30)

btn.place(x=325, y=350)

frame = Frame(win, width=1000, height=500)
frame.pack()
frame.place(anchor='nw', relx=0.275, rely=0)

response = requests.get("https://cdn.discordapp.com/attachments/979393895500763186/1011400679463583784/windws_39_lgo.png")
img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))

label = Label(frame, image = img)
label.pack()

# set window background color
win.configure(bg='blue')
win.mainloop()
