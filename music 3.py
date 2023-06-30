from tkinter import *
from pygame import mixer
from PIL import Image, ImageTk
from random import randint
import os
import sys
root=Tk()
mixer.init()
root.title('Music Player')
root.geometry("500x500")
sn=1
def update1():
    try:
        color="%05x" %randint(0,0xFFFFFF)
        root.config(background ='#fcba03' + color)
        root.after(1000, update1)
        #sngn.wm_attributes('-transparentcolor','#fcba03'+color)
        #sngn.config(bg='#fcba03'+color)
    except:
        update1()
update1()
s1=[]
sng_name=["Star Boy","SunFlower","Holiday","Calling"]
sngn=Label(root,text=sng_name[sn-1],font="gravis 20  bold")
sngn.place(relx=0.5,rely=0.1,anchor=CENTER)
music_status=False
def update():
    global sngname,sn
    image2=Image.open(f'p{sn}.jpg')
    img2=image2.resize((350, 350))
    my_img2=ImageTk.PhotoImage(img2)
    label.configure(image=my_img2)
    label.image=my_img2
    sngn.config(text=sng_name[sn-1])
    
image=Image.open('p1.jpg')

# Resize the image in the given (width, height)
img=image.resize((350, 350))

# Conver the image in TkImage
my_img=ImageTk.PhotoImage(img)

# Display the image with label
label=Label(root, image=my_img)
label.place(bordermode=INSIDE, height=350, width=350,relx=0.5,rely=0.5,anchor=CENTER)
songs = os.listdir(r"C:/Users/Santhosh/Desktop/Code Clause internship")
for song in songs:
    if song.endswith(".mp3"):
        s1.append(song)
def start():
    global music_status
    music_status=True
    global sn
    update()
    mixer.music.load(f"song{sn}.mp3")
    mixer.music.play()
def pause():
    global music_status
    if music_status==True:
        mixer.music.pause()
        music_status=False
    else:
        mixer.music.unpause()
        music_status=True
def exit():
    mixer.music.stop()
    sys.exit()
def next():
    global sn
    try:
        sn=sn+1
        start()
    except:
        sn=1
        start()
def prev():
    global sn,s1
    try:
        sn=sn-1
        start()
    except:
        sn=len(s1)
        start()
#icons for buttons
play_img=ImageTk.PhotoImage(Image.open("play.jpg").resize((40,40),Image.ANTIALIAS))
ps_img=ImageTk.PhotoImage(Image.open("pause.png").resize((40,40),Image.ANTIALIAS))
nxt_img=ImageTk.PhotoImage(Image.open("next.png").resize((40,40),Image.ANTIALIAS))
prev_img=ImageTk.PhotoImage(Image.open("prev.png").resize((40,40),Image.ANTIALIAS))
#buttons
strt=Button(root,command=start,image=play_img).place(relx = 0.55, rely = 0.95, anchor = S)
pse=Button(root,command=pause,image=ps_img).place(relx = 0.45, rely = 0.95, anchor = S)
#rsume=Button(root,command=resume,text="resume").place(relx = 0.6, rely = 0.95, anchor = S)
ext=Button(root,command=exit,text="exit" ,font="sans-serif 20 italic bold").grid(row=1,column=4)
nxt=Button(root,command=next,image=nxt_img).place(relx = 0.95, rely = 0.5, anchor = CENTER)
prev=Button(root,command=prev,image=prev_img).place(relx = 0.05, rely = 0.5, anchor = CENTER)
root.mainloop()