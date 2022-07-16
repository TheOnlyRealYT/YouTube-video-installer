from tkinter import *
from pytube import YouTube
from tkinter import filedialog

win = Tk(screenName='Py youtube video installer')
win.title('youtube installer')
win.geometry('400x300')
win.iconbitmap('logo.ico')

r = IntVar()
r.set(1)
type = ''
if r.get() == 1:
    typev = '.mp4'
else:
    typev = '.mp3'

def start():
    link = forminput.get()
    filename = forminput2.get()
    if link != "":
        vid = YouTube(link)
        if filename != "":
            vid.streams.first().download(filename=filename+typev)
        else:
            vid.streams.first().download(filename=vid.title+typev)

title = Label(win, text='PyTube video downloader')
prumt = Label(win, text='Enter the link: ')
forminput = Entry(win, width=50, borderwidth=0)
prumt2 = Label(win, text='What will you call it: ')
forminput2 = Entry(win, width=50, borderwidth=0)
Radiobutton(win, text='mp4-video', variable=r, value=1).place(x=10, y=140)
Radiobutton(win, text='mp3-audio', variable=r, value=2).place(x=10, y=160)
btn = Button(win, text='download', borderwidth=1, command=start)
text = Label(win, text='the files will be saved in the same directory as the app')

title.place(x=135, y=10)
prumt.place(x=10, y=50)
forminput.place(x=10, y=70)
prumt2.place(x=10, y=90)
forminput2.place(x=10, y=120)
btn.place(x=330, y=260)
text.place(x=5, y=200)
win.mainloop()