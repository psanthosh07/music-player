from tkinter import *
from pygame import mixer
import os



root=Tk()
mixer.init()
root.title('Music Player')
songs = os.listdir(r"C:/Users/Santhosh/Desktop/Code Clause internship")
sn=0
sl=[]
song_status=False
def start():
    global sn
    print(song_status)
    if not song_status:
        songs = os.listdir(r"C:/Users/Santhosh/Desktop/Code Clause internship")
        print(len(songs))
        for song in songs:
            if song.endswith(".mp3"):
                sl.append(song)
            print(sl)
        for i in range(sn,len(sl)):
            print(i)
            mixer.music.load(sl[0])
            mixer.music.play()
            print(f"2nd{sn}")
    if song_status:
        mixer.music.unpause()
def pause():
    global song_status
    song_status=True
    mixer.music.pause()
def next():
    global sn
    sn=sn+1
    print(sn)
    start()
def previ():
    global sn
    try:
        sn=sn-1
        start()
    except :
        sn=3
        start()
    
label1=Label(root,text="Song name").grid(row=0
strt=Button(root,text="Start",command =start).grid(row=1,column=1)
ps=Button(root,text="Pause",command=pause).grid(row=1,column=2)
nxt=Button(root,text="NEXT",command=next).grid(row=1,column=3)
prev=Button(root,text="Previous",command=previ).grid(row=1,column=4)
root.mainloop()

