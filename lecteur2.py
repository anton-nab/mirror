from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Spotify Musique")
root.geometry("920x670+290+85")
root.configure(bg="grey")
root.resizable(False, False)

mixer.init()


def ouvrir():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)


def playsong():
    music_name = playlist.get(ACTIVE)
    # print(music_name[0:-5])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-5])


# icon
image_icon = PhotoImage(
    file=r"D:\ynov\Science de l'ingénieur\image\spotify.png")
root.iconphoto(False, image_icon)

logo = PhotoImage(file=r"D:\ynov\Science de l'ingénieur\image\spotfy2.png")
Label(root, image=logo, bg="grey").place(x=30, y=30)

play = PhotoImage(file=r"D:\ynov\Science de l'ingénieur\image\play.png")
Button(root, image=play, bg="grey", bd=0, command=playsong).place(x=60, y=300)

pause = PhotoImage(file=r"D:\ynov\Science de l'ingénieur\image\pause.png")
Button(root, image=pause, bg="grey", bd=0).place(x=60, y=400)

skip = PhotoImage(file=r"D:\ynov\Science de l'ingénieur\image\skip.png")
Button(root, image=skip, bg="grey", bd=0).place(x=120, y=350)

previous = PhotoImage(
    file=r"D:\ynov\Science de l'ingénieur\image\previous.png")
Button(root, image=previous, bg="grey", bd=0).place(x=0, y=350)


# label

music = Label(root, text="SPOTIFY", font="arial 15", fg="green", bg="black")
music.place(x=80, y=150, anchor="center")

# music

music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=330, y=50, width=550, height=450)


Button(root, text="ouvrir fichier", width=15, height=2,
       font="arial 10 bold", fg="black", bg="grey", command=ouvrir).place(x=150, y=50)

scroll = Scrollbar(music_frame)

playlist = Listbox(music_frame, width=100, font="arial 10", bg="black",
                   fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)

playlist.pack(side=LEFT, fill=BOTH)


root.mainloop()
