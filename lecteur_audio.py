import tkinter as tk
import os
import fnmatch
from typing import Pattern

from pygame import *

canvas = tk.Tk()
canvas.title("Spotify Musique")
canvas.geometry("500x500")
canvas.config(bg="white")

rootpath = "D:\\ynov\Science de l'ingénieur\musique"
pattern = "*.mp3"

mixer.init()

prec_img = tk.PhotoImage(file="image/previous.png")
suiv_img = tk.PhotoImage(file="image/skip.png")
play_img = tk.PhotoImage(file="image/play.png")
pause_img = tk.PhotoImage(file="image/play_pause.png")


def select():
    label.config(text=listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()


def stop():
    mixer.music.stop()
    listbox.select_clear("active")


def suiv():
    next_song = listbox.curselection()
    next_song = next_song[0]+1
    next_song_name = listbox.get(next_song)

    label.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0, "end")
    listbox.activate(next_song)
    listbox.select_set(next_song)


def prec():
    prev_song = listbox.curselection()
    prev_song = prev_song[0]+1
    prev_song_name = listbox.get(prev_song)

    label.config(text=prev_song_name)
    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listbox.select_clear(0, "end")
    listbox.activate(prev_song)
    listbox.select_set(prev_song)


listbox = tk.Listbox(canvas, fg="white", bg="black",
                     width=100, font=('poppin', 14))
listbox.pack(padx=15, pady=15)

label = tk.Label(canvas, text="", bg="white", fg="black", font=('poppin', 18))
label.pack(pady=15)

top = tk.Frame(canvas, bg="white")
top.pack(padx=10, pady=5, anchor="center")

precButton = tk.Button(canvas, text="prec",
                       image=prec_img, bg="white", borderwidth=0, command=prec)
precButton.pack(pady=15, in_=top, side="left")
stopButton = tk.Button(canvas, text="stop",
                       image=pause_img, bg="white", borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side="left")
playButton = tk.Button(canvas, text="play",
                       image=play_img, bg="white", borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side="left")
suivButton = tk.Button(canvas, text="suiv",
                       image=suiv_img, bg="white", borderwidth=0, command=suiv)
suivButton.pack(pady=15, in_=top, side="left")


for root, dirs, files in os.walk(rootpath):

    for filename in fnmatch.filter(files, pattern):

        listbox.insert('end', filename)

canvas.mainloop()
