from tkinter import *
from tkinter import filedialog
from pygame import mixer


def addsong():
    songselect = filedialog.askopenfilenames(initialdir="Music/", title="Select songs", filetypes=(("mp3 files", "*.mp3"),))
    for s in songselect:
        listsongs.insert(END, s)

def playsong():
    song = listsongs.get(ACTIVE)
    song = f'{song}'
    mixer.music.load(song)
    mixer.music.play()

def stopsong():
    mixer.music.stop()
    listsongs.selection_clear(ACTIVE)

def pausesong():
    mixer.music.pause()

def resumesong():
    mixer.music.unpause()

def nxtsong():
    nextone =listsongs.curselection()
    nextone = nextone[0] + 1
    song = listsongs.get(nextone)
    song = f'{song}'
    mixer.music.load(song)
    mixer.music.play()
    listsongs.selection_clear(0, END)
    listsongs.activate(nextone)
    listsongs.selection_set(nextone)

def prevsong():
    prevone =listsongs.curselection()
    prevone = prevone[0] - 1
    song = listsongs.get(prevone)
    song = f'{song}'
    mixer.music.load(song)
    mixer.music.play()
    listsongs.selection_clear(0, END)
    listsongs.activate(prevone)
    listsongs.selection_set(prevone)

def deleteSong():
    currsong = listsongs.curselection()
    listsongs.delete(currsong[0])



window = Tk()
window.title("music player")
mixer.init()

my_menu = Menu(window)
window.config(menu=my_menu)


control_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=control_song_menu)

control_song_menu.add_command(label="Add songs", command=addsong)
control_song_menu.add_command(label="Delete song", command=deleteSong)

listsongs = Listbox(window, bg="black", fg="white", font=("arial"),height=12,width=47, selectmode=SINGLE, selectbackground="gray", selectforeground="black")
listsongs.grid(columnspan=9)

playBtn = Button(window, text="play", command=playsong, font=("arial", 15), width=7)
playBtn.grid(row=1, column=0)

pauseBtn = Button(window, text="pause", command=pausesong, font=("arial", 15), width=7)
pauseBtn.grid(row=1, column=1)

stopBtn = Button(window, text="Stop", command=stopsong, font=("arial", 15), width=7)
stopBtn.grid(row=1, column=2)

resumeBtn = Button(window, text="Resume", command=resumesong, font=("arial", 15), width=7)
resumeBtn.grid(row=1, column=3)

prevBtn = Button(window, text="Prev", command=prevsong, font=("arial", 15), width=7)
prevBtn.grid(row=1, column=4)

nextBtn = Button(window, text="Next", command=nxtsong, font=("arial", 15), width=7)
nextBtn.grid(row=1, column=5)




window.mainloop()
