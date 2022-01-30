import requests
import mysql.connector as m

con = m.connect(host='localhost', password='sql123', user='root')

if con.is_connected():
    print('connected')

# creating cursor object
cursor = con.cursor()

#cursor.execute('create database quaver')
cursor.execute("use quaver")

# creating music repository table
cursor.execute("create table music_repo(song_name varchar(12),\
album varchar(12),\
artist varchar(12), \
genre varchar(12),duration float(2),song_link varchar(250))")
con.commit()        

link1 = 'http://commondatastorage.googleapis.com/codeskulptor-demos/riceracer_assets/music/lose.ogg'
link2 = 'http://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Kangaroo_MusiQue_-_The_Neverwritten_Role_Playing_Game.mp3'
link3 = 'http://codeskulptor-demos.commondatastorage.googleapis.com/pang/paza-moduless.mp3'
link4 = 'http://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Sevish_-__nbsp_.mp3'
link5 = 'http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg'

cursor.execute("insert into music_repo values('Song 1', 'Album 1', 'Artist 1', 'Genre 1', 2.03, '{}')".format(link1))
cursor.execute("insert into music_repo values('Song 2', 'Album 2', 'Artist 2', 'Genre 2', 2.05, '{}')".format(link2))
cursor.execute("insert into music_repo values('Song 3', 'Album 3', 'Artist 3', 'Genre 3', 2.44, '{}')".format(link3))
cursor.execute("insert into music_repo values('Song 4', 'Album 4', 'Artist 4', 'Genre 4', 2.66, '{}')".format(link4))
cursor.execute("insert into music_repo values('Song 5', 'Album 5', 'Artist 5', 'Genre 5', 2.67, '{}')".format(link5))
       
# downloading songs onto local device from internet

cursor.execute("select song_link from music_repo")
data=cursor.fetchall()
a=1
var=data[0][0]
doc = requests.get(var)
with open('Beatz'+'.mp3', 'wb') as f:
        f.write(doc.content)

a=2
var=data[1][0]
doc = requests.get(var)
with open('shake it off'+'.mp3', 'wb') as f:
        f.write(doc.content)

a=3
var=data[2][0]
doc = requests.get(var)
with open('we are one'+'.mp3', 'wb') as f:
        f.write(doc.content)

a=4
var=data[3][0]
doc = requests.get(var)
with open('lets go home'+'.mp3', 'wb') as f:
        f.write(doc.content)

a=5
var=data[4][0]
doc = requests.get(var)
with open('believer'+'.mp3', 'wb') as f:
        f.write(doc.content)
        
con.commit()


#GUI

from tkinter import *
from tkinter import filedialog
import pygame
root = Tk()
root.title("QUAVER")
root.iconbitmap()
root.geometry("500x300")

pygame.mixer.init()

def play():
    song = songbox.get(ACTIVE)
    song = f"C:/Users/shrey/OneDrive/Documents/python shreya/{song}.mp3"

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True

def forward():
    nextsong = songbox.curselection()
    nextsong = nextsong[0]+1
    song = songbox.get(nextsong)
    song = f"C:/Users/shrey/OneDrive/Documents/python shreya/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.selection_clear(0, END)
    songbox.activate(nextsong)
    songbox.selection_set(nextsong, last=None)

def back():
    nextsong = songbox.curselection()
    nextsong = nextsong[0]-1
    song = songbox.get(nextsong)
    song = f"C:/Users/shrey/OneDrive/Documents/python shreya/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.selection_clear(0, END)
    songbox.activate(nextsong)
    songbox.selection_set(nextsong, last=None)
    
songbox = Listbox(root, bg ="black", fg ="white", width = 60, selectbackground='gray', selectforeground='black')
songbox.pack(pady=20)

backbuttonimage = PhotoImage(file='C:\\Users\\shrey\\OneDrive\\Documents\\quaver_compProject\\backward.png') #images to be downloaded so blank for now itll show blank on screen in place of button widget
forwardbuttonimage = PhotoImage(file='C:\\Users\\shrey\\OneDrive\\Documents\\quaver_compProject\\forward.png')
playbuttonimage = PhotoImage(file="C:\\Users\\shrey\\OneDrive\\Documents\\quaver_compProject\\play.png")
pausebuttonimage = PhotoImage(file='C:\\Users\\shrey\\OneDrive\\Documents\\quaver_compProject\\pause.png')
stopbuttonimage = PhotoImage(file="C:\\Users\\shrey\\OneDrive\\Documents\\quaver_compProject\\stop.png")

#frame
controlframe = Frame(root)
controlframe.pack()

backbutton = Button(controlframe, image=backbuttonimage,borderwidth = 0, command = back) 
#border0 to avoid having a box around
forwardbutton= Button(controlframe, image=forwardbuttonimage,borderwidth = 0, command = forward)
playbutton= Button(controlframe, image=playbuttonimage,borderwidth = 0, command=play)
pausebutton= Button(controlframe, image=pausebuttonimage,borderwidth = 0, command=lambda: pause(paused) )
stopbutton =Button(controlframe, image=stopbuttonimage,borderwidth = 0, command= stop)

#pushing it onto frame using grid rows and cols
backbutton.grid(row =0,column =0,padx =6)
forwardbutton.grid(row =0,column =1,padx =6)
playbutton.grid(row =0,column =2,padx =6)
pausebutton.grid(row =0,column =3,padx =6)
stopbutton.grid(row =0,column =4,padx =6)

def addsong():
    song = filedialog.askopenfilename(initialdir='C:\\Users\\shrey\\OneDrive\\Documents\\python shreya\\',title='Choose song', filetypes=(('mp3 Files', '*.mp3'),))
    song = song.replace(r"C:/Users/shrey/OneDrive/Documents/python shreya/", '')
    song = song.replace('.mp3', '')
    
    songbox.insert(END, song)
    
menu1 = Menu(root) # this is in root, not our frame
root.config(menu = menu1)
addsongmenu = Menu(menu1)
menu1.add_cascade(label = "Add A New Song", menu = addsongmenu)
addsongmenu.add_command(label = "Add song", command = addsong)

root.mainloop()
